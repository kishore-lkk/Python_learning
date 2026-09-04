import json 
import jsonschema
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="enter the file path, that has to be validated")
parser.add_argument("-s","--schema", type=str, help="enter the schema file location")
args = parser.parse_args()

with open(args.input, "r", encoding="utf-8") as rf:
    document = json.load(rf)
with open(args.schema, "r", encoding="utf-8") as rf:
    schema_doc = json.load(rf)


try:
    jsonschema.validate(instance=document, schema=schema_doc)
    print("validation is succesfull")
except jsonschema.ValidationError as e:
    print(f"""
Validation error !!!
Error reason : {e.message}
    """)