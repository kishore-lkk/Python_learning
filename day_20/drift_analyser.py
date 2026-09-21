import json

def drift_checker(arg1, arg2):
    newly_added = list(arg2.keys() - arg1.keys())
    removed = list(arg1.keys() - arg2.keys())
    common_keys = set(arg2.keys()) & set(arg1.keys())
    changed = {}
    for key in common_keys:
        if arg2[key] != arg1[key]:
            changed.update({key: {"old" : arg1[key], "new" : arg2[key]}})
        else:
            pass
    output= {}
    output.update({"newly_added":newly_added,"removed":removed,"changed":changed})
    return(output)
    


if __name__ == "__main__":
    try:
        with open("./1.txt", "r", encoding="utf-8") as first, open("./2.txt", "r", encoding="utf-8") as second, open("./ouput.txt", "w", encoding="utf-8") as wf:
            first = json.load(first)
            second = json.load(second)
            result = drift_checker(first, second)
            json.dump(result,wf,indent=4)
    except Exception as e:
        print(str(e))