import json
import argparse
import requests

def https_checker(input):
    https_checked = {"valid_urls" : {}, "invalid_urls" : {}}
    for line in input:
        try:
            https_checked["valid_urls"].update({line : requests.get(line,timeout=10).status_code})
        except Exception as reason:
            https_checked["invalid_urls"].update({line : str(reason)})
    return(https_checked)
    pass


def https_header_extractor(input):
    header_data = {}
    for line in input["valid_urls"]:
        content = requests.get(line).headers
        header_data.update({line : dict(content)})
    return(header_data)


parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="enter the file name")
args = parser.parse_args()

try:
    with open(args.file, "r", encoding="utf-8") as rf:
        content = json.load(rf)
        if isinstance(content, list):
            url_result = https_checker(content)
            result = https_header_extractor(url_result)
            with open("Learning/day_9/output.txt", "w", encoding="utf-8") as wf:
                json.dump(result, wf, indent=4)
        else:
            print("the input file should be list")
except Exception as e:
    print(e)