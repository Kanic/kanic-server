import urllib2
import json

from django.shortcuts import render, HttpResponse

from .models import Make, Model
from .utils import scrapeCarData


def addcar(request):
    theyear = 2016
    for i in range(27):
        name = None
        niceName = None
        name, niceName = scrapeCarData("https://api.edmunds.com/api/vehicle/v2/makes?state=used&year={0}&view=basic&fmt=json&api_key=kfsejvb5gbdhgqhke6xwv4wg".format(theyear))
        print len(name)
        for i, j in zip(name, niceName):
            make, created = Make.objects.get_or_create(name=i, niceName=j)
        theyear = theyear - 1

    return HttpResponse("aha")

def addmodel(request):
    theyear=2016
    for i in range(27):
        request = urllib2.urlopen("https://api.edmunds.com/api/vehicle/v2/makes?state=used&year={0}&view=basic&fmt=json&api_key=kfsejvb5gbdhgqhke6xwv4wg".format(theyear))
        myjson = json.loads(request.read())

        name = []
        niceName = []
        year = []
        makes = myjson["makes"]

        for make in makes:
            print make["niceName"]
            themake = Make.objects.get(niceName=make["niceName"])
            models = make["models"]
            for model in models:
                name = model["name"]
                niceName = model["niceName"]
                year = model["years"][0]["year"]
                model = Model(make=themake, name=name, niceName=niceName, years=year)
                model.save()

        theyear = theyear - 1

    return HttpResponse("addmodel")
