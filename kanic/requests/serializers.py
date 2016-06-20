from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.models import User, Mechanic
from .models import Service, Request


#################################Service###################################


class ServiceListSerializer(serializers.HyperlinkedModelSerializer):
    request_set = serializers.HyperlinkedRelatedField(
        view_name='request_retrieve_api',
        lookup_field='id',
        many=True,
        read_only=True
    )
    url = serializers.HyperlinkedIdentityField(view_name='service_retrieve_api', lookup_field='id')
    class Meta:
        model = Service
        fields = [
            'url',
            'id',
            'type',
            'tools',
            'request_set'
        ]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'type',
            'tools'
        ]


class ServiceUpdateSerializer(serializers.ModelSerializer):
    # request_set = RequestListSerializer()
    class Meta:
        model = Service
        fields = [
            # 'id',
            'type',
            # 'tools',
            # 'request_set'
        ]
        depth = 1



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
            'car',
            'service',
            'status',
            'extra_info',
        ]
        depth = 1


class RequestCreateSerializer(serializers.ModelSerializer):
    # car_owner = serializers.HyperlinkedRelatedField(
    #     view_name='user_retrieve_api',
    #     lookup_field='username',
    #     many=False,
    #     read_only=False
    # )
    # car_owner = serializers.SerializerMethodField()
    # service = serializers.CharField(source='service.id')
    # car_owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Request
        fields = [
            'id',
            'car_owner',
            'location',
            'scheduled_time',
            'car',
            'service',
            'status',
            'extra_info',
        ]

    # def get_car_owner(self, obj):
    #     queryset = User.objects.filter(id=obj.id)
    #     serializer = UserSerializer(queryset, context={"request": instance}, many=False)
    #     return serializer.data

    # def create(self, validated_data):
    #     car_owner_username = validated_data['car_owner']
    #     car_owner = User.objects.filter(username=car_owner_username)
    #     location = validated_data['location']
    #     scheduled_time = validated_data['scheduled_time']
    #     service_id = validated_data['service']
    #     service = Service.objects.filter(id=service_id)
    #     status = validated_data['status']
    #     extra_info = validated_data['extra_info']
    #     request = Request(car_owner=car_owner.id, location=location,
    #                       scheduled_time=scheduled_time, service=service.id,
    #                       status=status, extra_info=extra_info)
    #     request.save()
    #     return request



class RequestUpdateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='request_retrieve_api', lookup_field='id')
    # url = RequestUrlHyperlinkedIdentityField(view_name='request_retrieve_api')
    # car_owner = serializers.CharField(source='car_owner.username', read_only=True)
    # mechanic = serializers.CharField(source='mechanic.user.username', read_only=True)
    # service = serializers.CharField(source='service.type', read_only=True)
    # car_owner = serializers.HyperlinkedRelatedField(
    #     view_name='user_retrieve_api',
    #     lookup_field='username',
    #     many=False,
    #     read_only=True
    # )
    class Meta:
        model = Request
        fields = [
            # 'url',
            'id',
            'car_owner',
            'mechanic',
            'location',
            'scheduled_time',
            'car',
            'service',
            'status',
            'extra_info',
        ]
        depth = 1


# class RequestViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, ]
#     queryset = Request.objects.all()
#     serializer_class = RequestListSerializer
