#!/usr/bin/env python
# import requests
from urllib import FancyURLopener
import json
import sys

query = sys.argv[1]

class MyOpener(FancyURLopener):
    version = 'AppleWebKit/537.11 (KHTML, like Gecko) Safari/537.11'
    
site= "http://search.cocoapods.org/api/v1/pods.flat.hash.json?query={0}".format(query)
o = MyOpener()
results = json.loads(o.open(site).read())
output = []

for item in results:
    itemOut = {}
    itemOut["title"] = "{0}{1}".format(item["id"],item["version"])
    itemOut["subtitle"] = item["summary"]
    itemOut["url"] = "http://cocoadocs.org/docsets/{0}/{1}".format(item["id"], item["version"])
    output.append(itemOut)
    
print json.dumps(output)