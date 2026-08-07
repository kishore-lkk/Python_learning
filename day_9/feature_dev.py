import json
import requests

def https_header_extractor(input):
    header_data = {}
    for line in input["valid_urls"]:
        content = requests.get(line).headers
        header_data.update({line : dict(content)})
    return(header_data)


with open("Learning/day_9/input.txt", "r", encoding="utf-8") as rf:
    content = json.load(rf)
    result = https_header_extractor(content)
with open("Learning/day_9/header.json", "w", encoding="utf-8") as wf: 
    json.dump(result,wf, indent=4)