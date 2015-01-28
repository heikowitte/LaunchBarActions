#!/usr/bin/env python
import urllib2
import json
import sys

query = sys.argv[1]
output = []
results = json.loads(urllib2.urlopen("http://search.cocoapods.org/api/v1/pods.flat.hash.json?query={0}".format(query)).read())

for item in results:
    itemOut = {}
    itemOut["title"] = "{0}{1}".format(item["id"],item["version"])
    itemOut["subtitle"] = item["summary"]
    itemOut["url"] = "http://cocoadocs.org/docsets/{0}/{1}".format(item["id"], item["version"])
    output.append(itemOut)
    
print json.dumps(output)