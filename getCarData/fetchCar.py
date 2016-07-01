import requests
import json

def scrapeCarData():
    r = requests.get("https://api.edmunds.com/api/vehicle/v2/makes?state=new&year=2015&view=basic&fmt=json&api_key=kfsejvb5gbdhgqhke6xwv4wg")
    myjson = json.loads(r.text)

    name = []
    niceName = []
    makes = myjson["makes"]

    for make in makes:
        name.append(make["name"])
        niceName.append(make["niceName"])

    return name, niceName


name, niceName = scrapeCarData()

print name
