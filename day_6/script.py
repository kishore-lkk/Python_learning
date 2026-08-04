import re
import json 

with open("Learning/day_6/input.txt", 'r', encoding="utf-8") as rf:
    content = rf.read()

output = {}
output.update({"ipv4" : re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",content)})
output.update({"domains" : re.findall(r"[a-zA-Z0-9-]+\.[a-zA-Z]{2,}", content)})
output.update({"md5_hash" :re.findall(r"\b[a-fA-F0-9]{32}\b",content)})
output.update({"sha_1" : re.findall(r"\b[a-fA-F0-9]{40}\b",content)})
output.update({"sha_256" : re.findall(r"\b[a-fA-F0-9]{64}\b",content)})

with open("Learning/day_6/output.txt", "w", encoding="utf-8") as wf:
    json.dump(output,wf,indent=4)