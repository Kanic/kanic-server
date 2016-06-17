from django.shortcuts import render

from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser

from kanic.permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from .serializers import (RequestSerializer, RequestCreateSerializer, RequestUpdateSerializer,
ServiceListSerializer)
from .models import Service, Request


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    # queryset = Service.objects.all()
    def get_queryset(self):
        return Service.objects.all()


class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestSerializer
    # queryset = Request.objects.all()
    def get_queryset(self):
        return Request.objects.all()


class RequestCreateAPIView(generics.CreateAPIView):
    serializer_class = RequestCreateSerializer


class RequestRetrieveAPIView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestUpdateSerializer
    permission_classes = (IsOwnerOrAdmin,)
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
