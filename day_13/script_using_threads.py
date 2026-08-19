import json
import requests
import time 
from concurrent.futures import ThreadPoolExecutor


def https_request(content):
    with ThreadPoolExecutor() as executors:
      try:
        response = list(executors.map(requests.get,content))
        print(response)
      except Exception as e:
        print(str(e))




with open("Learning/day_13/input.txt", "r", encoding="utf-8") as rf:
    content = json.load(rf)
    https_request(content)

    