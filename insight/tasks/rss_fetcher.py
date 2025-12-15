from datetime import datetime
from typing import List, Dict
import feedparser


def fetch_rss(
    feed_url: str,
    source: str,
    limit: int = 20,
) -> List[Dict]:
    """
    RSS/Atom 피드를 수집하여 raw entry 리스트로 반환
    """
    feed = feedparser.parse(feed_url)

    if feed.bozo:
        raise ValueError(f"Invalid RSS feed: {feed_url}")

    items: List[Dict] = []

    for entry in feed.entries[:limit]:
        published_at = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_at = datetime(*entry.published_parsed[:6])

        items.append({
            "source": source,
            "title": entry.get("title"),
            "link": entry.get("link"),
            "summary": entry.get("summary"),
            "published_at": published_at,
            "fetched_at": datetime.utcnow(),
        })

    return items
