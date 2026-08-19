import json
import requests
import time 
from concurrent.futures import ThreadPoolExecutor
import argparse

def https_request(content):
    url_response = {}
    wait_time = 1
    for attempt, i in enumerate(range(3)):
        try:
            response = requests.get(content, timeout=5)
            url_response.update({"status" : "success"})
            url_response.update({"status_code" : response.status_code})
            url_response.update({"attempt" : attempt + 1})
            break
        except requests.exceptions.ConnectionError as e:
            error = type(e).__name__
            wait_time *= 2
            time.sleep(wait_time)
    else:
        url_response.update({"status" : "failed"})
        url_response.update({"error" : error})
        url_response.update({"attempt" : attempt + 1})
    return(content,url_response)

start = time.time()
with open("Learning/day_13/input.txt", "r", encoding="utf-8") as rf:
    content = json.load(rf)
    with ThreadPoolExecutor() as executors:
        output = dict(executors.map(https_request, content))

with open("Learning/day_13/output.txt", "w", encoding="utf-8") as wf:
    json.dump(output,wf, indent=4)
print("time taken ",time.time() - start)