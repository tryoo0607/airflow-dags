import feedparser
import logging
from typing import Any, Dict, List
from datetime import datetime

log = logging.getLogger(__name__)


class RSSFetchError(Exception):
    pass


def fetch_rss(source: Dict[str, Any]) -> List[Dict[str, Any]]:
    rss = source.get("rss")
    if not rss:
        raise RSSFetchError(f"RSS url missing: {source}")

    feed = feedparser.parse(
        rss,
        request_headers={
            "User-Agent": "rss-collector/1.0"
        }
    )

    if feed.bozo:
        log.warning(
            "RSS parse error: source=%s error=%s",
            source.get("name"),
            feed.bozo_exception,
        )

    entries = []
    for entry in feed.entries or []:
        entries.append({
            "entry": entry,
            "rss": rss,
            "source": source.get("name"),
            "fetched_at": datetime.utcnow(),
        })

    log.info(
        "Fetched RSS: source=%s entries=%d",
        source.get("name"),
        len(entries),
    )

    return entries