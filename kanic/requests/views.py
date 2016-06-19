from django.shortcuts import render, get_object_or_404

from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from kanic.permissions import IsOwnerOrReadOnly, IsOwnerOrAdminRequest
from .serializers import (RequestListSerializer, RequestCreateSerializer, RequestUpdateSerializer,
ServiceListSerializer, ServiceUpdateSerializer)
from .models import Service, Request


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    # queryset = Service.objects.all()
    def get_queryset(self):
        return Service.objects.all()

class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.all()


class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestListSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 10
    def get_queryset(self):
        return Request.objects.all()


class RequestCreateAPIView(generics.CreateAPIView):
    serializer_class = RequestCreateSerializer
    # permission_classes = (IsOwnerOrAdminRequest,)
    # queryset = Request.objects.all()
    # lookup_field = 'id'


class RequestRetrieveAPIView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestUpdateSerializer
    permission_classes = (IsOwnerOrAdminRequest,)

    def get_object(self):
        queryset = self.get_queryset()
        id = self.kwargs['id']
        obj = get_object_or_404(queryset, id=id)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class RequestListForUserAPIView(generics.ListAPIView):
    serializer_class = RequestCreateSerializer
    queryset = Request.objects.all()

    def list(self, request):
        queryset = Request.objects.filter(car_owner = request.user)
        serializer = RequestCreateSerializer(queryset, many=True)
        return Response(serializer.data)
