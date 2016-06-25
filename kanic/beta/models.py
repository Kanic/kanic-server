from django.db import models
from django.utils import timezone

class Tester(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    zipCode = models.CharField(max_length=7)
    car = models.BooleanField(default=False)
    createAt = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name
