import json
from pathlib import Path
from typing import List, Dict


def save_to_file(
    items: List[Dict],
    output_dir: str = "data/rss",
) -> None:
    """
    RSS 데이터를 JSONL 형태로 파일 저장
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_file = Path(output_dir) / "rss_items.jsonl"

    with output_file.open("a", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, default=str, ensure_ascii=False) + "\n")