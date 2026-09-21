import requests
import json


with open("Learning/day_19/sample_output.txt", "w",encoding="utf-8") as wf: 
    json.dump(requests.get("https://api.github.com/repos/microsoft/vscode").json(), wf, indent=4)