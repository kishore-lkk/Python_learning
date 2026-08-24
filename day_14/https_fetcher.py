import json
import requests
import time 
import argparse
from concurrent.futures import ThreadPoolExecutor


def https_reponse(url):
    wait_time = 1
    url_response = {}
    response = None
    url_response.update({"url" : url})
    for attempt, retry in enumerate(range(3)):
        try:
            response = requests.get(url, timeout=10)
            url_response.update({"status" : True})
            url_response.update({"status_code" : response.status_code})
            url_response.update({"attempts" : attempt + 1})
            break
        except requests.exceptions.ConnectionError as e:
            time.sleep(wait_time)
            wait_time *= 2
            error = type(e).__name__ 
    else:
        url_response.update({"status" : False})
        url_response.update({"reason" : error})
        url_response.update({"attempts" : attempt + 1})
    with_header_data = response_header(url_response ,response)
    return(with_header_data)

def response_header(url_response, requset_response):
    headers_data = {}
    if url_response["status"]:
        try:
            headers_data.update({"content-type" : requset_response.headers.get('Content-Type')})
            headers_data.update({"server" : requset_response.headers.get('Server')})
            headers_data.update({"content-length" : requset_response.headers.get('Content-Length')})
        except Exception:
            pass
    else:
        pass
    url_response.update({"header" : headers_data})

    return(url_response)

def response_cookies():

    return()

def main():
    with open("Learning/day_14/input.txt", "r", encoding="utf-8") as rf:
        url_list = [url.strip() for url in rf]
        with ThreadPoolExecutor() as executors:
            result = list(executors.map(https_reponse, url_list))
    print(result)
    



if __name__ == "__main__":
    main()
