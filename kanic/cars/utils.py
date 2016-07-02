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


# def scrapeModelData(url):
#     request = urllib2.urlopen(url)
#     myjson = json.loads(request.read())
#
#     name = []
#     niceName = []
#     year = []
#     makes = myjson["makes"]
#
#     for make in makes:
#         for model in make["models"]:
#             name = model["name"]
#             niceName = model["niceName"]
#             year = model["years"][0]["year"]
#
#             print name, niceName, year
#
#     for make in makes:
#         name.append(make["name"])
#         niceName.append(make["niceName"])
#
#     return name, niceName
