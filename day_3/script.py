import json 
import datetime 
import os 

output = {
    "metadata": {
        "generated_at":"",
        "source_file":"",
        "tool":"",
        "total_input":"",
        "total_valid":"",
        "invalid_count":""
    }
}


with open("Learning/day_2/input.json", "r", encoding="utf-8") as invalid_url:
    output["metadata"].update({"total_input":str(len(invalid_url.readlines()))})
invalid_url.close()
with open("Learning/day_3/input.json", "r", encoding="utf-8") as rf:
    content = json.load(rf)
    output["metadata"].update({"generated_at":str(datetime.datetime.now())})
    output["metadata"].update({"source_file":rf.name})
    output["metadata"].update({"tool":os.path.basename(__file__)})
    output["metadata"].update({"total_valid" : len(content["valid_url"]) })
    output["metadata"].update({"invalid_count" : int(output["metadata"]["total_input"]) - int(output["metadata"]["total_valid"])})
    output.update(content)
rf.close()

with open("Learning/day_3/output.json", "w", encoding="utf-8") as wf:
    json.dump(output,wf,indent=4)
