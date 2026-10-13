from bs4 import BeautifulSoup as bs
from bs4 import Comment
import requests
import argparse
import json 
import re
 
def get_link(soup):
    extracted_link = []
    for link in soup.find_all("a", attrs={'href' : re.compile(r"^https://")}):
        extracted_link.append(link.get('href'))
    return extracted_link

def get_form(soup):
    form_data = []
    for form in soup.find_all("form"):
        form_info = {
            "action" : form.get("action"),
            "method" : form.get("method"),
            "input" : []
        }
        for inp in form.find_all("input"):
            form_info["input"].append({
                "name":inp.get("name"),
                "type" : inp.get("type")
            })
        form_data.append(form_info)
    return(form_data)

def get_comment(soup):
    extracted_comments = []
    comments = soup.find_all(string = lambda text: isinstance(text, Comment))
    for comment in comments:
        extracted_comments.append(comment.strip())
    return extracted_comments

def main():
    try:
        #parser = argparse.ArgumentParser
        #parser.add_argument("-u","--url",type="str",help="enter the url")
        #arg = parser.parse_args()
        arg = "https://cksbakery.com/"
        respone = requests.get(arg).text
        soup = bs(respone, "html.parser")
        output = {}
        output.update({"links" : get_link(soup)})
        output.update({"forms" : get_form(soup)})
        output.update({"comments": get_comment(soup)})
    except Exception as e:
        print(str(e))
    finally:
        with open("Learning/day_21/website_soucecode.json", "w", encoding="utf-8") as wf:
            json.dump(output, wf, indent=4)
    pass

if __name__ == "__main__":
    main()