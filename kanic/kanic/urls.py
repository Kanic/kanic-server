"""kanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from users.serializers import UserViewSet, MechanicViewSet
from requests.serializers import RequestViewSet, ServiceViewSet
from users.views import UserListAPIView, UserRetrieveAPIView, UserCreateAPIView


router = routers.DefaultRouter()
router.register(r'mechanics', MechanicViewSet)
router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'requests', RequestViewSet)

from kanic import views

urlpatterns = [
    url(r'^api2/beta/users/create/?$', UserCreateAPIView.as_view(), name='user_create_api'),
    url(r'^api2/beta/users/?$', UserListAPIView.as_view(), name='user_list_api'),
    url(r'^api2/beta/users/(?P<username>[\w-]+)/?$', UserRetrieveAPIView.as_view(), name='user_retrieve_api'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', views.home, name='home'),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]
