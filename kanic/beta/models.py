import json

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
    email = models.EmailField(verbose_name='email address',
                                      max_length=255,
                                      unique=True)

    def __unicode__(self):
        return self.email


class Job(models.Model):
    title = models.CharField(verbose_name='job title', max_length=255)
    code = models.CharField(verbose_name='job code', max_length=255, unique=True)
    requirement = models.CharField(verbose_name='job requirements',
                                   max_length=3000)
    responsibility = models.CharField(verbose_name='job responsibility',
                                      max_length=3000)
    description = models.CharField(verbose_name='job description',
                                   max_length=3000)
    job_types = (
        ('in', 'internship'),
        ('pt', 'part-time'),
        ('ft', 'full-time'),
    )
    type = models.CharField(verbose_name='job type',
                                   max_length=3000)
    salary = models.CharField(verbose_name='job salary',
                                   max_length=30)

    def __unicode__(self):
        return self.title

    def set_requirement(self, requirements):
        self.requirement = json.dumps(requirements)

    def get_requirement(self):
        return json.loads(self.requirement)

    def set_responsibility(self, responsibilities):
        self.responsibility = json.dumps(responsibilities)

    def get_responsibility(self):
        return json.loads(self.responsibility)


class HiringJob(models.Model):
    job = models.ForeignKey(Job)
    resume = models.FileField(upload_to='upload/')
    createAt = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        try:
            return self.job.title
        except:
            return 'Do not have a job title'
