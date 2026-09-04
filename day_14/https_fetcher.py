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
        except requests.exceptions.RequestException as e:
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
    headers_check = []
    check_flags = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"]
    if url_response["status"]:
        try:
            headers_data.update({"content-type" : requset_response.headers.get('Content-Type')})
            headers_data.update({"server" : requset_response.headers.get('Server')})
            headers_data.update({"content-length" : requset_response.headers.get('Content-Length')})
            for flag in check_flags:
                if flag not in requset_response.headers:
                    headers_check.append(flag)
                    url_response.update({"missing_headers" : headers_check})
        except Exception as e:
            print(str(e))
    else:
        pass
    url_response.update({"header" : headers_data})
    url_response.update({"missing_headers" : headers_check})
    with_cookies_data = response_cookies(url_response, requset_response)
    return(with_cookies_data)

def response_cookies(url_response, requset_response):
    cookies_checker = {}
    try:
        for cookie in requset_response.cookies:
            cookies_checker[cookie.name] = {}
            if cookie.secure:
                cookies_checker[cookie.name].update({"secure" : "present"})
            else:
                cookies_checker[cookie.name].update({"secure" : "missing"})
            if cookie._rest.get("SameSite") != "None" and cookie._rest.get("SameSite") != None:
                cookies_checker[cookie.name].update({"SameSite" : "present"})
            else:
                cookies_checker[cookie.name].update({"SameSite" : "missing"})   
            if cookie._rest.get("HttpOnly"):
                cookies_checker[cookie.name].update({"HttpOnly" : "present"})
            else:
                cookies_checker[cookie.name].update({"HttpOnly" : "missing"})          
    except Exception as e:
        pass
    url_response.update({"cookies" : cookies_checker})
    return(url_response)





def main():
    with open("Learning/day_14/input.txt", "r", encoding="utf-8") as rf:
        url_list = [url.strip() for url in rf]
        with ThreadPoolExecutor() as executors:
            result = list(executors.map(https_reponse, url_list))
    with open("Learning/day_14/output.txt", "w", encoding="utf-8") as wf:
        json.dump(result, wf, indent=4)

if __name__ == "__main__":
    main()
