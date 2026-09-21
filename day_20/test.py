import json

if __name__ == "__main__":
    try:
        with open("./1.txt", "r", encoding="utf-8") as first, open("./2.txt", "r", encoding="utf-8") as second:
            first = json.load(first)
            second = json.load(second)
            print(first.values())
    except Exception as e:
        print(str(e))