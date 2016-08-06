from django.shortcuts import render, get_object_or_404

from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from kanic.permissions import IsOwnerOrReadOnly, IsOwnerOrAdminRequest
from .serializers import (RequestListSerializer, RequestCreateSerializer,
                          RequestUpdateSerializer, ServiceListSerializer,
                          ServiceUpdateSerializer)
from .models import Service, Request


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    
    def get_queryset(self):
        return Service.objects.all()

class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceUpdateSerializer
    lookup_field = "id"
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

    def perform_create(self, serializer):
        serializer.save(car_owner=self.request.user, mechanic=None)


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
    serializer_class = RequestUpdateSerializer

    def get_queryset(self):
        return Request.objects.get_current_user_request(self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RequestUpdateSerializer(queryset, many=True)
        return Response(serializer.data)
