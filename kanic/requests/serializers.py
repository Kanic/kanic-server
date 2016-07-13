from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Service, Request
from users.models import User, Mechanic
from cars.models import Make, Model

# from users.serializers import CarOwnerSerializer



#################################Service###################################


class ServiceListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='service_retrieve_api', lookup_field='id')
    class Meta:
        model = Service
        fields = [
            'url',
            'id',
            'name',
            'part',
            'detail',
            'price'
        ]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'part',
            'detail',
            'price'
        ]


class ServiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'id',
            'name',
            'part',
            'detail',
            'price'
        )



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



class RequestListSerializer(serializers.ModelSerializer):
    car_owner = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = [
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

    def get_car_owner(self, obj):
        data = obj.car_owner.get_nested_attributes_for_serializer()
        return data


class RequestCreateSerializer(serializers.ModelSerializer):
    car_owner = serializers.SerializerMethodField()
    mechanic = serializers.PrimaryKeyRelatedField(many=False,
                                                  read_only=True,
                                                  required=False)
    car = serializers.PrimaryKeyRelatedField(many=False, queryset=Model.objects.all())
    service = serializers.PrimaryKeyRelatedField(many=False, queryset=Service.objects.all())

    class Meta:
        model = Request
        fields = (
            'id',
            'car_owner',
            'mechanic',
            'car',
            'service',
            'location',
            'scheduled_time',
            'status',
            'extra_info',
        )
        depth = 1

    def get_car_owner(self, obj):
        data = obj.car_owner.get_nested_attributes_for_serializer()
        return data

    # def create(self, validated_data):
    #     return Request(**validated_data).save()

    # def create(self, validated_data):
    #     car_owner= validated_data.get('car_owner')
    #     location = validated_data.get('location')
    #     scheduled_time = validated_data.get('scheduled_time')
    #     service = validated_data['service']
    #     status = validated_data['status']
    #     extra_info = validated_data['extra_info']
    #     request = Request(car_owner=car_owner.id, location=location,
    #                       scheduled_time=scheduled_time, service=service.id,
    #                       status=status, extra_info=extra_info)
    #     request.save()
    #     return request



class RequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
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
        depth = 2


# class RequestViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, ]
#     queryset = Request.objects.all()
#     serializer_class = RequestListSerializer
