from django.contrib import admin

from .models import Request, Service

admin.site.register(Request)
admin.site.register(Service)
