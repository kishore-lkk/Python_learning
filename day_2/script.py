import json
import urllib.parse as url

def validation(input):
    parser = url.urlsplit(input)
    if parser.scheme == "":
        input = "https://" + input
        parser = url.urlsplit(input)
    print(parser)
    return()


def normalization(input):
    return()




with open("Learning/day_2/input.json", "r", encoding="utf-8") as rf:
    input = json.load(rf)
    for line in input:
        validated_result = validation(line)
        nomralized_result = normalization(validated_result)