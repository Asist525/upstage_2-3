import json
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RULES_PATH = BASE_DIR / "rules.json"

with open(RULES_PATH, "r", encoding="utf-8") as f:
    rules = json.load(f)

documents = [r["content"] for r in rules]
metadatas = rules

res = requests.post(
    "http://localhost:8800/knowledge",
    json={
        "documents": documents,
        "metadatas": metadatas,
    }
)

print(res.status_code)
print(res.json())
