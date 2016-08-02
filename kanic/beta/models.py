from django.db import models
from django.utils import timezone


class Tester(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    zipCode = models.CharField(max_length=7)
    car = models.BooleanField(default=False)
    createAt = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class BetaMechanic(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_certified = models.BooleanField(default=False)
    certification = models.CharField(max_length=40, null=True, blank=True)

    work_type_choices = (
        ('FT', 'Full Time'),
        ('PT', 'Part Time')
    )
    work_type = models.CharField(max_length=40, choices=work_type_choices)
    createAt = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Newsletter(models.Model):
    email = email = models.EmailField(verbose_name='email address',
                                      max_length=255,
                                      unique=True)

    def __unicode__(self):
        return self.email
