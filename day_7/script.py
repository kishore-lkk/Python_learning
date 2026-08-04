import re
import json
import urllib.parse as url
import ipaddress
import datetime
import os
from collections import Counter
import argparse

def ioc_extract(content):
    output = {}
    output.update({"ipv4" : re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",content)})
    output.update({"domains" : re.findall(r"(?:https?://)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}", content)})
    output.update({"md5_hash" : re.findall(r"\b[a-fA-F0-9]{32}\b",content)})
    output.update({"sha_1" : re.findall(r"\b[a-fA-F0-9]{40}\b",content)})
    output.update({"sha_256" : re.findall(r"\b[a-fA-F0-9]{64}\b",content)})
    return(output)

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


def metadata_attacher(valid_url, invalid_count, filename):
    output = {
        "metadata": {
            "generated_at":"",
            "source_file":"",
            "tool":"",
            "total_input":"",
            "total_valid":"",
            "invalid_count":""
        }
    }

    output["metadata"].update({"total_input": invalid_count})
    output["metadata"].update({"generated_at":str(datetime.datetime.now())})
    output["metadata"].update({"source_file": filename})
    output["metadata"].update({"tool":os.path.basename(__file__)})
    output["metadata"].update({"total_valid" : len(valid_url["valid_url"]) })
    output["metadata"].update({"invalid_count" : int(output["metadata"]["total_input"]) - int(output["metadata"]["total_valid"])})
    output.update(valid_url)
    return(output)

def output_presenter(input):
    output = {}
    frequent_url = Counter()
    url_list = list()
    for counter, line in enumerate(input):
        domain = url.urlsplit(line).hostname
        url_list.append(domain)
    frequent_url.update(url_list)
    output.update({"total_urls" : counter + 1})
    output.update({"unique_domains" : len(frequent_url.keys())})
    output.update({"domain_frequency" : frequent_url.most_common(3)})

    print(f''' 
{"*"*50}

Output is saved to output.json file
* {'total url count is :':50} {counter + 1}
* {'unique url count is :':<50} {output["unique_domains"]}
* {'frequently appearing domains :':<50} {output["domain_frequency"]}

{"*"*50}''')

    pass


# main statement


parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["extraction","validation"], type=str, help="determines the mode")
parser.add_argument("-f","--file",type=str,help="enter the file path")
args = parser.parse_args()


try:
    if args.mode == "extraction":
        with open(args.file, "r", encoding="utf-8") as rf:
            content = rf.read()
        ioc = ioc_extract(content)
        with open("Learning/day_7/output.json" ,'w', encoding="utf-8") as wf:
            json.dump(ioc, wf, indent=4)
        print("IOC are extracted and saved to output.json")
    elif args.mode == "validation":
        with open(args.file, "r", encoding="utf-8") as rf:
            valid_url = {}
            valid_url.setdefault("valid_url",[])
            try:
                input = json.load(rf)
                if isinstance(input, list):
                    for counter, line in enumerate(input):
                        validated_result = validation(line)
                        nomralized_result = normalization(validated_result)
                        if nomralized_result:
                            valid_url['valid_url'].append(nomralized_result)
                    metadata_added = metadata_attacher(valid_url, counter + 1, str(rf.name))
                    with open("Learning/day_7/output.json", "w", encoding="utf-8") as wf:
                        json.dump(metadata_added, wf, indent=4)
                    output_presenter(valid_url["valid_url"])
                else:
                    print("list is needed as input")
            except Exception as e:
                print(e)
except Exception as e:
    print(e)
