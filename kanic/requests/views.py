from django.shortcuts import render, get_object_or_404

from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser

from kanic.permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from .serializers import (RequestListSerializer, RequestCreateSerializer, RequestUpdateSerializer,
ServiceListSerializer, ServiceUpdateSerializer)
from .models import Service, Request


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    # queryset = Service.objects.all()
    def get_queryset(self):
        return Service.objects.all()

class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceUpdateSerializer


class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestListSerializer
    paginate_by = 10
    def get_queryset(self):
        return Request.objects.all()


class RequestCreateAPIView(generics.CreateAPIView):
    serializer_class = RequestCreateSerializer


class RequestRetrieveAPIView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestUpdateSerializer
    permission_classes = (IsOwnerOrAdmin,)

    def get_object(self):
        queryset = self.get_queryset()
        id = self.kwargs['id']
        obj = get_object_or_404(queryset, id=id)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
