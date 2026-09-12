"""Fetch Google Scholar metrics into results/ for the google-scholar-stats branch.

GitHub Actions IPs are datacenter ranges that Google Scholar regularly
challenges. The old scholarly + FreeProxies path made that worse: scholarly
issues several follow-up requests, and public proxies are already on Google's
block lists, so a blocked run failed in seconds instead of succeeding on a
later attempt.

This crawler instead:

1. Requests the public author profile once (pagesize=100 covers this CV).
2. Prefers Chrome TLS impersonation so the handshake does not look like
   Python-requests, which Scholar fingerprints.
3. Parses citations / h-index / i10 / papers from that single HTML page.
4. Refuses to publish an empty or implausible payload, so a CAPTCHA page
   cannot wipe the numbers on the site.
"""

from __future__ import annotations

import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"

SCHOLAR_ID_DEFAULT = "k3BMw_QAAAAJ"
PROFILE_URL = (
    "https://scholar.google.com/citations?user={sid}&hl=en&cstart=0&pagesize=100"
)
BROWSER_HEADERS = {
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
}
BLOCK_MARKERS = (
    "gs_captcha",
    "unusual traffic",
    "not a robot",
    "sorry/index",
    "enable javascript",
)
STATS_RE = re.compile(r'<td class="gsc_rsb_std">([0-9,]+)</td>')
NAME_RE = re.compile(r'<div id="gsc_prf_in">([^<]+)</div>')
AFFIL_RE = re.compile(r'<div class="gsc_prf_il">([^<]+)</div>')
EMAIL_RE = re.compile(r'id="gsc_prf_ivh">Verified email at ([^< ]+)')
HOMEPAGE_RE = re.compile(r'class="gsc_prf_ila" href="([^"]+)"')
INTEREST_RE = re.compile(r'class="gsc_prf_inta[^"]*"[^>]*>([^<]+)')
ROW_RE = re.compile(r'<tr class="gsc_a_tr">(.*?)</tr>', re.DOTALL)
PUB_ID_RE = re.compile(r"citation_for_view=([^\"&]+)")
PUB_TITLE_RE = re.compile(r'class="gsc_a_at"[^>]*>([^<]+)')
PUB_CITES_RE = re.compile(r'class="gsc_a_ac gs_ibl"[^>]*>([0-9,]*)')
PUB_YEAR_RE = re.compile(r'class="gsc_a_h[^"]*"[^>]*>([0-9]{4})')
CITES_ID_RE = re.compile(r"[?&]cites=([0-9]+)")


class Blocked(Exception):
    pass


def _int(value, default=0):
    try:
        return int(str(value).replace(",", "").strip() or default)
    except (TypeError, ValueError):
        return default


def _looks_blocked(html):
    text = html.lower()
    if any(marker in text for marker in BLOCK_MARKERS):
        return True
    if 'id="gsc_prf_in"' not in html and "gsc_rsb_std" not in html:
        return True
    return False


def fetch_html_chrome(url):
    from curl_cffi import requests as cffi_requests

    response = cffi_requests.get(
        url,
        impersonate="chrome",
        timeout=30,
        headers={"Accept-Language": BROWSER_HEADERS["Accept-Language"]},
    )
    response.raise_for_status()
    return response.text


def fetch_html_urllib(url):
    request = urllib.request.Request(
        url,
        headers={
            **BROWSER_HEADERS,
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, "replace")


def fetch_profile_html(scholar_id):
    url = PROFILE_URL.format(sid=scholar_id)
    attempts = [
        ("chrome-tls", fetch_html_chrome),
        ("urllib", fetch_html_urllib),
    ]
    last_error = None
    for label, fetcher in attempts:
        try:
            print(f"[scholar] GET {url} via {label}", flush=True)
            html = fetcher(url)
        except ImportError as exc:
            last_error = exc
            print(f"[scholar] {label} unavailable: {exc}", flush=True)
            continue
        except (urllib.error.URLError, OSError, Exception) as exc:
            last_error = exc
            print(f"[scholar] {label} failed: {type(exc).__name__}: {exc}", flush=True)
            continue
        if _looks_blocked(html):
            last_error = Blocked(f"{label} returned a challenge page ({len(html)} bytes)")
            print(f"[scholar] {last_error}", flush=True)
            continue
        print(f"[scholar] {label} returned {len(html)} bytes", flush=True)
        return html
    raise Blocked(f"all fetchers failed; last error: {last_error}")


def parse_publications(html, scholar_id):
    publications = {}
    for row in ROW_RE.findall(html):
        pub_id_match = PUB_ID_RE.search(row)
        if not pub_id_match:
            continue
        pub_id = unescape(pub_id_match.group(1))
        if not pub_id.startswith(f"{scholar_id}:"):
            continue
        title_match = PUB_TITLE_RE.search(row)
        year_match = PUB_YEAR_RE.search(row)
        cites_match = PUB_CITES_RE.search(row)
        cites_id_match = CITES_ID_RE.search(row)
        num_citations = _int(cites_match.group(1) if cites_match else 0)
        cites_id = cites_id_match.group(1) if cites_id_match else None
        publications[pub_id] = {
            "container_type": "Publication",
            "source": "AUTHOR_PUBLICATION_ENTRY",
            "bib": {
                "title": unescape(title_match.group(1)).strip() if title_match else "",
                "pub_year": year_match.group(1) if year_match else "",
            },
            "filled": False,
            "author_pub_id": pub_id,
            "num_citations": num_citations,
            "citedby_url": (
                f"https://scholar.google.com/scholar?oi=bibs&hl=en&cites={cites_id}"
                if cites_id
                else None
            ),
            "cites_id": [cites_id] if cites_id else [],
        }
    return publications


def parse_author(html, scholar_id):
    stats = [_int(value) for value in STATS_RE.findall(html)]
    if len(stats) < 6:
        raise Blocked(f"citation table missing (parsed {stats!r})")
    citedby, citedby5y, hindex, hindex5y, i10index, i10index5y = stats[:6]
    name_match = NAME_RE.search(html)
    affil_match = AFFIL_RE.search(html)
    email_match = EMAIL_RE.search(html)
    homepage_match = HOMEPAGE_RE.search(html)
    publications = parse_publications(html, scholar_id)
    return {
        "container_type": "Author",
        "filled": ["basics", "publications", "indices", "counts"],
        "scholar_id": scholar_id,
        "source": "AUTHOR_PROFILE_PAGE",
        "name": unescape(name_match.group(1)).strip() if name_match else "",
        "affiliation": unescape(affil_match.group(1)).strip() if affil_match else "",
        "interests": [unescape(item).strip() for item in INTEREST_RE.findall(html)],
        "email_domain": email_match.group(1) if email_match else "",
        "homepage": unescape(homepage_match.group(1)) if homepage_match else "",
        "citedby": citedby,
        "citedby5y": citedby5y,
        "hindex": hindex,
        "hindex5y": hindex5y,
        "i10index": i10index,
        "i10index5y": i10index5y,
        "publications": publications,
    }


def fetch_author(scholar_id):
    retries = int(os.environ.get("SCHOLAR_RETRIES", "3"))
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            html = fetch_profile_html(scholar_id)
            return parse_author(html, scholar_id)
        except Blocked as exc:
            last_error = exc
            print(f"[scholar] attempt {attempt}/{retries} blocked: {exc}", flush=True)
            if attempt < retries:
                delay = random.uniform(8, 20)
                print(f"[scholar] retrying in {delay:.1f}s", flush=True)
                time.sleep(delay)
    raise RuntimeError(f"could not fetch a usable Scholar profile: {last_error}")


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip() or SCHOLAR_ID_DEFAULT
    author = fetch_author(scholar_id)
    citedby = author.get("citedby") or 0
    publications = author.get("publications") or {}

    if citedby < 1 or len(publications) < 1:
        sys.exit(
            f"[scholar] implausible result (citedby={citedby}, "
            f"publications={len(publications)}); refusing to overwrite"
        )

    author["updated"] = str(datetime.now())

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    (RESULTS_DIR / "gs_data.json").write_text(
        json.dumps(author, ensure_ascii=False)
    )
    (RESULTS_DIR / "gs_data_shieldsio.json").write_text(
        json.dumps(
            {"schemaVersion": 1, "label": "citations", "message": f"{citedby}"},
            ensure_ascii=False,
        )
    )
    print(
        f"[scholar] wrote results/: citedby={citedby}, "
        f"hindex={author.get('hindex')}, publications={len(publications)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
