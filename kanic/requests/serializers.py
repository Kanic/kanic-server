from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Service, Request


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'type',
            'tools',
            'car',
        ]


class ServiceViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    # car_owner = serializers.UserSerializer(many=False, read_only=True)
    class Meta:
        model = Request
        fields = [
            'id',
            'car_owner',
            'mechanic',
            'location',
            'scheduled_time',
            'service',
            'status',
            'extra_info',
        ]


class RequestViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
