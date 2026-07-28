import json
import urllib.parse as url
import ipaddress
import re

def validation(input):
    parser = url.urlsplit(input)
    if parser.scheme == "":
        input = "https://" + input
        parser = url.urlsplit(input)
    if re.match(r'^[0-9.]+$', parser.hostname):
        try:
            if ipaddress.ip_address(parser.hostname):
                return(parser)
        except Exception:
            pass
    elif " " not in parser.netloc and "." in parser.netloc:
        return(parser)
    pass

def normalization(input):
    try:
        if re.search(r'[A-Z]', input.netloc):
            corrected_url = input.scheme + "://" + input.netloc.lower() + input.path + input.query + input.fragment
            return(corrected_url)

        else:
            final_url = url.urlunsplit(input)
            return(final_url)
    except Exception:
        pass  

    return()

with open("Learning/day_2/input.json", "r", encoding="utf-8") as rf:
    with open("Learning/day_2/output.json", "w", encoding="utf-8") as wf:
        valid_url = {}
        valid_url.setdefault("valid_url",[])
        input = json.load(rf)
        for line in input:
            validated_result = validation(line)
            nomralized_result = normalization(validated_result)
            if nomralized_result:
                valid_url['valid_url'].append(nomralized_result)
        json.dump(valid_url, wf, indent= 4)
    wf.close()
rf.close()