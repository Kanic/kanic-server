from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# from users.serializers import UserSerializer
from users.models import User, Mechanic
from .models import Service, Request


#################################Service###################################


class ServiceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'type',
            'tools',
            'car',
        ]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'type',
            'tools',
            'car',
        ]

class ServiceUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'type',
            'tools',
            'car',
        ]


# class ServiceViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, ]
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer


#################################Request###################################

# this can be user for two or more url endpoints
# class RequestUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
#     def get_url(self, obj, view_name, request, format):
#         kwargs = {
#             'id': obj.id
#         }
#         return reverse(view_name, kwargs=kwargs, request=request, format=format)



class RequestListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='request_retrieve_api', lookup_field='id')
    # car_owner = serializers.CharField(source='car_owner.username', read_only=True)
    car_owner = serializers.HyperlinkedRelatedField(
        view_name='user_retrieve_api',
        lookup_field='username',
        many=False,
        read_only=True
    )
    service = serializers.HyperlinkedRelatedField(
        view_name='service_retrieve_api',
        lookup_field='id',
        many=False,
        read_only=True
    )
    # car_owner = UserSerializer()
    mechanic = serializers.CharField(source='mechanic.user.username', read_only=True)

    class Meta:
        model = Request
        fields = [
            'url',
            'id',
            'car_owner',
            'mechanic',
            'location',
            'scheduled_time',
            'service',
            'status',
            'extra_info',
        ]


class RequestCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = [
            'car_owner',
            'location',
            'scheduled_time',
            'service',
            'status',
            'extra_info',
        ]


class RequestUpdateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='request_retrieve_api', lookup_field='id')
    # url = RequestUrlHyperlinkedIdentityField(view_name='request_retrieve_api')
    # car_owner = serializers.CharField(source='car_owner.username', read_only=True)
    # mechanic = serializers.CharField(source='mechanic.user.username', read_only=True)
    # car_owner = serializers.HyperlinkedRelatedField(
    #     view_name='user_retrieve_api',
    #     lookup_field='username',
    #     many=False,
    #     read_only=True
    # )
    class Meta:
        model = Request
        fields = [
            'url',
            'id',
            'car_owner',
            'mechanic',
            'location',
            'scheduled_time',
            'service',
            'status',
            'extra_info',
        ]


# class RequestViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, ]
#     queryset = Request.objects.all()
#     serializer_class = RequestListSerializer
