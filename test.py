import json

with open("Learning/day_3/input.json", "r", encoding="utf-8") as rf:
    content = json.load(rf)
    count = 0
    for lines in content["valid_url"]:
        count += 1

    print(count)