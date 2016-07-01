from django.shortcuts import render, HttpResponse

from .models import Make
from .utils import scrapeCarData


def addcar(request):
    name = None
    niceName = None
    if request.method == 'GET':
        name, niceName = scrapeCarData("https://api.edmunds.com/api/vehicle/v2/makes?state=new&year=2015&view=basic&fmt=json&api_key=kfsejvb5gbdhgqhke6xwv4wg")

    for i, j in zip(name, niceName):
        make = Make(name=i, niceName=j)
        make.save()

    return HttpResponse("aha")
