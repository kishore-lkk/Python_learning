from bs4 import BeautifulSoup as bs
import requests

url = "https://cksbakery.com"
response = requests.get(url).text
output = bs(response, "html.parser").prettify()
with open("Learning/day_21/source_code.html", "w", encoding='utf-8') as wf:
    wf.write(output)

