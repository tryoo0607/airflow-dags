from typing import List, Dict
from hashlib import sha256
def normalize_rss_items(items: List[Dict]) -> List[Dict]:
    normalized: List[Dict] = []

    for item in items:
        title = (item.get("title") or "").strip()
        link = (item.get("link") or "").strip()

        unique_key = sha256(f"{title}{link}".encode("utf-8")).hexdigest()

        normalized.append({
            "id": unique_key,
            "source": item.get("source"),
            "title": title,
            "link": link,
            "summary": item.get("summary"),
            "published_at": item.get("published_at"),
            "fetched_at": item.get("fetched_at"),
        })

    return normalized
