RSS_FIELD_MAPPING = {
    # 네이버 블로그
    "rss.blog.naver.com": {
        "title": ["title"],
        "url": ["link"],
        "content": ["summary"],
        "published_at": ["published_parsed"],
        "author": ["author", "dc_creator"],
    },

    # Tistory
    "tistory.com/rss": {
        "title": ["title"],
        "url": ["link"],
        "content": ["summary", "content[0].value"],
        "published_at": ["published_parsed", "updated_parsed"],
        "author": ["author"],
    },

    # Medium
    "medium.com/feed": {
        "title": ["title"],
        "url": ["link"],
        "content": ["content[0].value", "summary"],
        "published_at": ["published_parsed"],
        "author": ["author"],
    },
}