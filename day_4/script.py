import json

file_name = input("Enter the file name: ")

error = {}
with open("Learning/day_4/error.json", "w", encoding="utf-8") as wf:
    try :
        with open(file_name, "r", encoding="utf-8") as rf:
            try:
                content = json.load(rf)
                if isinstance(content, list):
                    with open("Learning/day_4/valid.json", "w", encoding="utf-8") as wf_1:
                        json.dump(content,wf_1,indent=4)
                else:
                    error.update({"error" : "list is needed"})
                    json.dump(error,wf)
                   
            except Exception as e:
                error.update({"error" : str(e)})
                json.dump(error, wf)
    except Exception as e:
        error.update({"error" : str(e)})
        json.dump(error, wf)
