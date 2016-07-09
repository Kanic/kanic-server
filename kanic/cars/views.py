# import urllib2
# import json

from django.shortcuts import render, HttpResponse
from django.db.models.query import QuerySet

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Make, Model
# from .utils import scrapeCarData

from .serializers import (ModelListSerializer, ModelRetrieveSerializer,
                          MakeListSerializer, MakeListWithModelsSerializer)



class MakeListAPIView(generics.ListAPIView):
    serializer_class = MakeListSerializer
    queryset = Make.objects.all()

    def get_queryset(self):
        if self.request.query_params.get('niceName', ''):
            niceName = self.request.query_params['niceName']
            return Make.objects.filter(niceName=niceName)
        else:
            return Make.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        if request.query_params.get('has_model_set', ''):
            if request.query_params['has_model_set'] in ('True', 'true', True):
                serializer = MakeListWithModelsSerializer(queryset, many=True)
            else:
                serializer = MakeListSerializer(queryset, many=True)
        else:
            serializer = MakeListSerializer(queryset, many=True)

        return Response(serializer.data)


class ModelListAPIView(generics.ListAPIView):
    serializer_class = ModelListSerializer

    def get_queryset(self):
        models = None
        if self.request.query_params.get('make', ''):
            param_make = self.request.query_params.get('make')
            make = Make.objects.get(niceName=param_make)
            models = make.model_set.all()
            if self.request.query_params.get('year', ''):
                year = self.request.query_params.get('year')
                if year.isdigit():
                    year = int(year)
                else:
                    year = 0
                models = models.filter(years=year)
            return models
        else:
            return Model.objects.all()

    def list(self, request):
        if request.query_params.get('make', ''):
            param_make = request.query_params.get('make')
            try:
                Make.objects.get(niceName=param_make)
            except Make.DoesNotExist:
                response = {'error': 'make does not exist'}
                return Response(response)

        queryset = self.get_queryset()
        serializer = ModelListSerializer(queryset, many=True)

        return Response(serializer.data)


class YearListWithMakeAPIView(APIView):

    def get(self, request, format=None):
        response = []
        if request.query_params.get('make', ''):
            make_query = None
            niceName = request.query_params.get('make')
            try:
                make_query = Make.objects.get(niceName=niceName)
            except Make.DoesNotExist:
                return Response([])
            makes = [make_query]
        else:
            makes = Make.objects.all()
        for make in makes:
            singleMake = {}
            years = []
            singleMake['make_id'] = make.id
            singleMake['name'] = make.name
            singleMake['niceName'] = make.niceName
            models = make.model_set.all()
            for model in models:
                if model.years in years:
                    pass
                else:
                    years.append(model.years)
            singleMake['years'] = years
            response.append(singleMake)

        return Response(response)



# def addcar(request):
#     theyear = 2016
#     for i in range(27):
#         name = None
#         niceName = None
#         name, niceName = scrapeCarData("https://api.edmunds.com/api/vehicle/v2/makes?state=used&year={0}&view=basic&fmt=json&api_key=kfsejvb5gbdhgqhke6xwv4wg".format(theyear))
#         print len(name)
#         for i, j in zip(name, niceName):
#             make, created = Make.objects.get_or_create(name=i, niceName=j)
#         theyear = theyear - 1
#
#     return HttpResponse("aha")
#
# def addmodel(request):
#     theyear=2016
#     for i in range(27):
#         request = urllib2.urlopen("https://api.edmunds.com/api/vehicle/v2/makes?state=used&year={0}&view=basic&fmt=json&api_key=kfsejvb5gbdhgqhke6xwv4wg".format(theyear))
#         myjson = json.loads(request.read())
#
#         name = []
#         niceName = []
#         year = []
#         makes = myjson["makes"]
#
#         for make in makes:
#             print make["niceName"]
#             themake = Make.objects.get(niceName=make["niceName"])
#             models = make["models"]
#             for model in models:
#                 name = model["name"]
#                 niceName = model["niceName"]
#                 year = model["years"][0]["year"]
#                 model = Model(make=themake, name=name, niceName=niceName, years=year)
#                 model.save()
#
#         theyear = theyear - 1
#
#     return HttpResponse("addmodel")
