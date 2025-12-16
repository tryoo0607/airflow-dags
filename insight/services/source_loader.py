import yaml
import requests

DB_YAML_URL = "https://raw.githubusercontent.com/awesome-devblog/awesome-devblog/main/db.yml"

def load_source() :
    resp = requests.get(DB_YAML_URL, timeout=10)
    resp.raise_for_status()
    return yaml.safe_load(resp.text)