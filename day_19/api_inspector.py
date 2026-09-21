import requests
import argparse
import json

def requestor(arg):
    output = {}
    prefix = ""
    try:
        response = requests.get(arg).json()
        if isinstance(response, list):
            list_inspected = list_inspector(response, output, prefix)
            return list_inspected
        elif isinstance(response, dict):
            dict_inspected = dict_inspector(response, output, prefix)
            return dict_inspected
        else:
            print("response is not list or dict")
    except Exception as e:
        print(str(e))

def list_inspector(arg, output, prefix):
    list_output = []
    for line in arg:
        output = {}
        list_output.append(dict_inspector(line, output, prefix))
    return list_output

def dict_inspector(arg,output,prefix):
    for line in arg:
        if isinstance(arg[line], dict):
            dict_inspector(arg[line], output, prefix = prefix + line + ".")
        else:
            if prefix:
                output.update({prefix + line : arg[line]})
            else:
                output.update({line : arg[line]})
    return output
        

def main(): 
    output = requestor("https://api.github.com/repos/microsoft/vscode")
    with open("Learning/day_19/output.txt", "w", encoding="utf-8") as wf:
        json.dump(output,wf, indent=4)
    print(f"output is saved in the file ouput.txt")

if __name__ == "__main__":
    main()