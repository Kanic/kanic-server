# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=80)),
                ('scheduled_time', models.DateTimeField(verbose_name=b'scheduled_date_time')),
                ('car', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('extra_info', models.CharField(max_length=200, null=True, blank=True)),
                ('car_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('mechanic', models.ForeignKey(blank=True, to='users.Mechanic', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=40)),
                ('tools', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.ForeignKey(blank=True, to='requests.Service', null=True),
        ),
    ]
