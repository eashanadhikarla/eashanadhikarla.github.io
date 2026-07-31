"""Fetch Google Scholar metrics into results/ for the google-scholar-stats branch.

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

REPO_ROOT = Path(__file__).resolve().parent.parent
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

    # A blocked or partial scrape can return an empty profile; publishing that
    # would wipe the numbers shown on the site.
    if not citedby or not publications:
        sys.exit(f"[scholar] implausible result (citedby={citedby}, publications={len(publications)})")

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
    print(
        f"[scholar] wrote results/: citedby={citedby}, publications={len(publications)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
