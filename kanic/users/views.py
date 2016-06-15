from django.shortcuts import render, get_object_or_404

from rest_framework import generics, permissions, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User, Mechanic
from .serializers import UserSerializer, UserCreateSerializer, UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserListAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        return User.objects.all()

class UserRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self):
        queryset = self.get_queryset()
        # obj = get_object_or_404(queryset, self.lookup_field)
        print self.lookup_field
        username = self.kwargs['username']
        obj = get_object_or_404(queryset, username=username)
        return obj
