import json
import argparse
import time
import requests
from pathlib import Path

def https_request(args):
    url_response = {}
    wait_time = 1
    for line in args:
        wait_time = 1
        url_response.update({line : {}})
        for attempt, iteration in enumerate(range(3)):
            try:
                    response = requests.get(line, timeout=5)
                    url_response[line].update({"status" : "success"})
                    url_response[line].update({"status_code" : response.status_code})
                    url_response[line].update({"attempts" : attempt + 1})
                    break
            except requests.exceptions.ConnectionError as e:
                error = type(e).__name__
                wait_time *= 2
                time.sleep(wait_time)
        else:
            url_response[line].update({"status" : "failed"})
            url_response[line].update({"reason" : error})
            url_response[line].update({"attempts" : attempt + 1})
    return(url_response)


start = time.time()
content = json.loads(Path("Learning/day_12/input.txt").read_text(encoding="utf-8"))
try:
    if isinstance(content, list):
        output = https_request(content)
        Path("Learning/day_12/output.txt").write_text(json.dumps(output, indent=4),encoding="utf-8")
except Exception as e:
    print(str(e))

print("time taken is ",time.time() - start)

