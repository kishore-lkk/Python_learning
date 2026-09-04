import requests

def headers(url):
    response = requests.get(url, timeout=10, allow_redirects=True).headers
    return(response)
