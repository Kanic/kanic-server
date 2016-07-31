from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from requests.serializers import RequestListSerializer
from .models import User, Mechanic


################################Mechanic###########################


# Mechanic serializers
class MechanicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mechanic
        fields = (
            'id',
            'year_of_experience',
            'address',
        )

# class MechanicViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, ]
#     queryset = Mechanic.objects.all()
#     serializer_class = MechanicSerializer


################################User###########################
class UserSerializer(serializers.ModelSerializer):
    mechanic = MechanicSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone',
            'first_name',
            'last_name',
            'is_mechanic',
            'mechanic',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'password',
            'is_mechanic',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.is_mechanic = validated_data['is_mechanic']
        try:
            user.first_name = validated_data['first_name']
            user.last_name = validated_data['last_name']
        except KeyError:
            print("first_name and last_name were not provided.")
        user.save()
        return user


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone',
            'first_name',
            'last_name',
            'is_mechanic',
            'mechanic'
        )


class CarOwnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone',
            'first_name',
            'last_name',
            'request_set',
        )
        depth = 1
