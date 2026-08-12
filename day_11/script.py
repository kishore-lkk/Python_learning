import json 
import requests
import argparse


def cookie_audit(content):
    cookies_checker = {}
    flag_list = ["secure", "SameSite", "HttpOnly"]
    for url in content:
        cookies_checker[url] = {}
        response = requests.get(url)
        for cookie in response.cookies:
            dict_cookie = vars(cookie)
            cookies_checker[url][dict_cookie["name"]] = {}
            for flag in flag_list:
                if flag == "secure":
                    if dict_cookie[flag]:
                        cookies_checker[url][dict_cookie["name"]].update({flag : "present"})
                    else:
                        cookies_checker[url][dict_cookie["name"]].update({flag : "missing"})
                else:
                    if flag in dict_cookie["_rest"]:
                        cookies_checker[url][dict_cookie["name"]].update({flag : "present"})
                    else:
                        cookies_checker[url][dict_cookie["name"]].update({flag : "missing"})


                    
    return(cookies_checker)


with open("Learning/day_11/input.json", "r", encoding="utf-8") as rf:
    content = json.load(rf)
result = cookie_audit(content)
with open("Learning/day_11/output.json", "w", encoding="utf-8") as wf:
    json.dump(dict(result), wf, indent=4)