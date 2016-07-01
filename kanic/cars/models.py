from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=20)
    niceName = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey(Make)
    name = models.CharField(max_length=40)
    niceName = models.CharField(max_length=40)
    years = models.IntegerField()

    def __unicode__(self):
        return self.name
