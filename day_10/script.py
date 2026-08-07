import json

def header_checker(content):
    result = {}
    check_flags = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"]
    for line in content:
            result[line] = {}
            for flags in check_flags:
                 if flags in content[line]["headers"]:
                      result[line].setdefault("present",[]).append(flags)
                 else:
                      result[line].setdefault("missing",[]).append(flags)

    return(result)





with open("Learning/day_10/input.json", "r", encoding="utf-8") as rf:
    content = json.load(rf)
output = header_checker(content)
with open("Learning/day_10/output.json", "w", encoding="utf-8") as wf:
     json.dump(output,wf, indent=4)