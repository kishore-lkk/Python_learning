import requests


def header(url):
    header_dict = {}
    header_data = requests.get(url).headers
    header_dict.update({"content-type" : header_data['Content-Type']})
    header_dict.update({"server" : header_data['Server']})
    print(header_dict)





with open("Learning/day_14/input.txt", "r", encoding="utf-8") as rf:
    url_list = [ url.strip() for url in rf]
    output = [header(url) for url in url_list]
