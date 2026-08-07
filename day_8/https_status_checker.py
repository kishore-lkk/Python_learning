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


parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="enter the file name")
args = parser.parse_args()

try:
    with open(args.file, "r", encoding="utf-8") as rf:
        content = json.load(rf)
        if isinstance(content, list):
            result = https_checker(content)
            with open("Learning/day_8/output.txt", "w", encoding="utf-8") as wf:
                json.dump(result, wf, indent=4)
        else:
            print("the input file should be list")
except Exception as e:
    print(e)