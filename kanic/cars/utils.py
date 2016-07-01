import urllib2
import json

def scrapeCarData(url):
    request = urllib2.urlopen(url)
    myjson = json.loads(request.read())

    name = []
    niceName = []
    makes = myjson["makes"]

    for make in makes:
        name.append(make["name"])
        niceName.append(make["niceName"])

    return name, niceName
