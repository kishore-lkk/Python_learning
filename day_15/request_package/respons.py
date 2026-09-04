import requests

def response(url):
    response = requests.get(url, timeout=10, allow_redirects=True)
    return(response)
