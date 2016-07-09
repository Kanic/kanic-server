from django.db import models
from django.utils import timezone

from users.models import User, Mechanic
from cars.models import Model


class Service(models.Model):
    name = models.CharField(max_length=40)
    part = models.CharField(max_length=100, null=True, blank=True)
    detail = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    createAt = models.DateTimeField(default=timezone.now)
    lastModified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name


class Request(models.Model):
    car_owner = models.ForeignKey(User)
    mechanic = models.ForeignKey(Mechanic, null=True, blank=True)
    car = models.ForeignKey(Model, null=True, blank=True)
    service = models.ForeignKey(Service, null=True, blank=True)
    location = models.CharField(max_length=80)
    scheduled_time = models.DateTimeField('scheduled_date_time')
    status = models.IntegerField(default=0)
    extra_info = models.CharField(max_length=200, null=True, blank=True)
    createAt = models.DateTimeField(default=timezone.now)
    lastModified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        try:
            return "{0}, {1}, status: {2}".format(self.car_owner.last_name, self.service.name, self.status)
        except AttributeError:
            return "{0}, {1}".format(self.car_owner.last_name, self.status)
