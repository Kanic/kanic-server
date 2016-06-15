from django.db import models
from users.models import User, Mechanic

class Service(models.Model):
    type = models.CharField(max_length=40)
    tools = models.CharField(max_length=100)
    car = models.CharField(max_length=20)


class Request(models.Model):
    car_owner = models.ForeignKey(User)
    mechanic = models.ForeignKey(Mechanic, null=True, blank=True)
    location = models.CharField(max_length=80)
    scheduled_time = models.DateTimeField('scheduled_date_time')
    service = models.ForeignKey(Service, null=True, blank=True)
    status = models.IntegerField(default=0)
    extra_info = models.CharField(max_length=200, null=True, blank=True)
