def extract(entry: dict, path: str):
    cur = entry
    for part in path.split("."):
        if "[" in part:
            key, idx = part.rstrip("]").split("[")
            cur = cur.get(key, [])
            cur = cur[int(idx)] if len(cur) > int(idx) else None
        else:
            cur = cur.get(part)

        if cur is None:
            return None
    return cur
