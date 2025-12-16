from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Article:
    title: str
    url: str
    content: str
    published_at: Optional[datetime]
    author: Optional[str]