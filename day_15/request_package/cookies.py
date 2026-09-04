import requests

def cookies(url):
    response = requests.get(url, timeout=10, allow_redirects=True).cookies.get_dict()
    return(response)
