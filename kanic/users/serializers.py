from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from requests.serializers import RequestSerializer
from .models import User, Mechanic


# Mechanic serializers
class MechanicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mechanic
        fields = [
            'id',
            'year_of_experience',
            'address',
        ]


# User serializers
class UserUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'username': obj.username
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = UserUrlHyperlinkedIdentityField(view_name='user_retrieve_api')
    mechanic = MechanicSerializer(many=False, read_only=True)
    request_set = RequestSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_mechanic',
            'mechanic',
            'request_set',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_mechanic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MechanicViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
