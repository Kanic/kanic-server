from django.shortcuts import render, get_object_or_404

from rest_framework import generics, permissions, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from kanic.permissions import IsOwner, IsOwnerOrAdminUser
from .models import User, Mechanic
from .serializers import UserSerializer, UserCreateSerializer, CarOwnerListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JSONWebTokenAuthentication
    ]
    serializer_class = UserCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserListAPIView(generics.ListAPIView):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JSONWebTokenAuthentication
    ]
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdminUser,)

    def get_object(self):
        queryset = self.get_queryset()
        username = self.kwargs['username']
        obj = get_object_or_404(queryset, username=username)
        return obj


class CarOwnerListAPIView(generics.ListAPIView):
    serializer_class = CarOwnerListSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return User.objects.filter(is_mechanic=False)
