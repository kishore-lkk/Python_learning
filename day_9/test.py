import requests
import json

content = requests.get("https://owasp.org/").headers
with open("Learning/day_9/header.json", "w", encoding="utf-8") as wf:
    json.dump(dict(content), wf, indent=4)