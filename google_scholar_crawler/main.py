"""Fetch Google Scholar metrics and write them to _data/scholar_stats.yml.

Google Scholar blocks datacenter IPs, so a direct fetch succeeds from a laptop
but not from a CI runner. The fetch is therefore attempted directly first and
then through free proxies, under a hard deadline so a blocked scrape fails
instead of hanging until the CI job is killed.
"""

import json
import os
import signal
import socket
import sys
from datetime import datetime
from pathlib import Path

from scholarly import ProxyGenerator, scholarly

# Publication totals exclude two Scholar entries that are not standalone papers.
PUBLICATION_OFFSET = 2

REPO_ROOT = Path(__file__).resolve().parent.parent
STATS_FILE = REPO_ROOT / "_data" / "scholar_stats.yml"
RESULTS_DIR = REPO_ROOT / "results"

DEADLINE_SECONDS = int(os.environ.get("SCHOLAR_DEADLINE_SECONDS", "600"))
SOCKET_TIMEOUT_SECONDS = 30


class Timeout(Exception):
    pass


def _raise_timeout(signum, frame):
    raise Timeout(f"exceeded {DEADLINE_SECONDS}s deadline")


def fetch_author(scholar_id):
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    return author


def fetch_with_fallback(scholar_id):
    """Try a direct fetch, then proxied fetches; return the first success."""
    attempts = [("direct", None)]
    attempts += [(f"free-proxy #{i + 1}", "free") for i in range(3)]

    last_error = None
    for label, mode in attempts:
        try:
            if mode == "free":
                pg = ProxyGenerator()
                if not pg.FreeProxies():
                    raise RuntimeError("no free proxy available")
                scholarly.use_proxy(pg)
            print(f"[scholar] attempting fetch via {label}...", flush=True)
            author = fetch_author(scholar_id)
            print(f"[scholar] success via {label}", flush=True)
            return author
        except Timeout:
            raise
        except Exception as exc:  # noqa: BLE001 - any scrape failure should fall through
            last_error = exc
            print(f"[scholar] {label} failed: {type(exc).__name__}: {exc}", flush=True)

    raise RuntimeError(f"all fetch attempts failed; last error: {last_error}")


def previous_citedby():
    """Read the last known citation count so we can sanity-check a new one."""
    if not STATS_FILE.exists():
        return None
    for line in STATS_FILE.read_text().splitlines():
        if line.startswith("citedby:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None


def write_stats(citedby, raw_pub_count, updated):
    publication_count = max(raw_pub_count - PUBLICATION_OFFSET, 0)
    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATS_FILE.write_text(
        f"citedby: {citedby}\n"
        f"publication_count: {publication_count}\n"
        f"publication_count_raw: {raw_pub_count}\n"
        f'updated: "{updated}"\n'
    )
    print(
        f"[scholar] wrote {STATS_FILE.relative_to(REPO_ROOT)}: "
        f"citedby={citedby}, publications={publication_count} (raw={raw_pub_count})",
        flush=True,
    )


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        sys.exit("GOOGLE_SCHOLAR_ID is not set")

    socket.setdefaulttimeout(SOCKET_TIMEOUT_SECONDS)
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _raise_timeout)
        signal.alarm(DEADLINE_SECONDS)

    try:
        author = fetch_with_fallback(scholar_id)
    except Timeout as exc:
        sys.exit(f"[scholar] aborted: {exc}")
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)

    citedby = author.get("citedby")
    publications = author.get("publications") or []
    raw_pub_count = len(publications)

    # A blocked or partial scrape can return an empty profile; refuse to
    # overwrite known-good numbers with it.
    if not citedby or raw_pub_count == 0:
        sys.exit(f"[scholar] implausible result (citedby={citedby}, publications={raw_pub_count})")

    last = previous_citedby()
    if last is not None and citedby < last * 0.5:
        sys.exit(f"[scholar] refusing suspicious drop: {last} -> {citedby}")

    updated = datetime.utcnow().strftime("%Y-%m-%d")
    write_stats(citedby, raw_pub_count, updated)

    # Retained for the shields.io badge and any consumer of the raw profile.
    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in publications}
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    (RESULTS_DIR / "gs_data.json").write_text(json.dumps(author, ensure_ascii=False))
    (RESULTS_DIR / "gs_data_shieldsio.json").write_text(
        json.dumps(
            {"schemaVersion": 1, "label": "citations", "message": f"{citedby}"},
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
