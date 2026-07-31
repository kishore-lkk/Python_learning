import json 
import urllib.parse as url
from collections import Counter

output = {}
frequent_url = Counter()
url_list = list()

with open("Learning/day_5/input.json", "r", encoding="utf-8") as rf:
    content = json.load(rf)
    for counter, line in enumerate(content):
        domain = url.urlsplit(line).hostname
        url_list.append(domain)
    frequent_url.update(url_list)
    output.update({"total_urls" : counter + 1})
    output.update({"unique_domains" : len(frequent_url.keys())})
    output.update({"domain_frequency" : frequent_url.most_common(3)})
    print(frequent_url)

with open("Learning/day_5/output.json", "w", encoding="utf-8") as wf:
    json.dump(output,wf, indent=4)


print(f''' 
********************

Output is saved to output.json file
* total url count is {counter + 1}
* unique url count is {output["unique_domains"]}
* frequently appearing domains : {output["domain_frequency"]}

*********************
''')