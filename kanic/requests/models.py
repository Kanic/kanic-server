from django.db import models
from django.utils import timezone
from users.models import User, Mechanic


class Service(models.Model):
    type = models.CharField(max_length=40)
    tools = models.CharField(max_length=100)
    createAt = models.DateTimeField(default=timezone.now)
    lastModified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.type


class Request(models.Model):
    car_owner = models.ForeignKey(User)
    mechanic = models.ForeignKey(Mechanic, null=True, blank=True)
    location = models.CharField(max_length=80)
    scheduled_time = models.DateTimeField('scheduled_date_time')
    car = models.CharField(max_length=50)
    service = models.ForeignKey(Service, null=True, blank=True)
    status = models.IntegerField(default=0)
    extra_info = models.CharField(max_length=200, null=True, blank=True)
    createAt = models.DateTimeField(default=timezone.now)
    lastModified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return "%s, %s"%(self.car_owner.last_name, self.service.type)
