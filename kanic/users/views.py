from django.shortcuts import render, get_object_or_404

from rest_framework import generics, permissions, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from kanic.permissions import IsOwner, IsOwnerOrAdminUser
from .models import User, Mechanic
from .serializers import (UserSerializer, UserCreateSerializer,
                          CarOwnerListSerializer, UserRetrieveSerializer)


class UserCreateAPIView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, JSONWebTokenAuthentication]
    serializer_class = UserCreateSerializer
    # permission_classes = (permissions.IsAdminUser,)


class UserListAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, JSONWebTokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return User.objects.all()


class UserRetrieveAPIView(generics.ListAPIView):
    def list(self, request):
        queryset = request.user
        serializer = UserRetrieveSerializer(queryset, many=False)
        return Response(serializer.data)


class CarOwnerListAPIView(generics.ListAPIView):
    serializer_class = CarOwnerListSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return User.objects.all_car_owner()
