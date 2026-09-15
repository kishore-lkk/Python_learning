import requests
import argparse
import json
from concurrent.futures import ThreadPoolExecutor

def to_get_response(args):
    session = requests.session()
    response = session.get(args)
    return(response.status_code)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file",type=str,help="enter the file path")
    args = parser.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as rf, open("Learning/day_18/output.txt", "w", encoding="utf-8") as wf:
            with ThreadPoolExecutor() as executor:
                response_list =list(executor.map(to_get_response,[line.strip() for line in rf]))
            json.dump(response_list,wf)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()