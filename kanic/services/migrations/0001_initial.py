# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=80)),
                ('scheduled_time', models.DateTimeField(verbose_name=b'scheduled_date_time')),
                ('status', models.IntegerField(default=0)),
                ('extra_info', models.CharField(max_length=200, null=True, blank=True)),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(blank=True, to='cars.Model', null=True)),
                ('car_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('mechanic', models.ForeignKey(blank=True, to='users.Mechanic', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('part', models.CharField(max_length=100, null=True, blank=True)),
                ('detail', models.CharField(max_length=200, null=True, blank=True)),
                ('price', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.ForeignKey(blank=True, to='services.Service', null=True),
        ),
    ]
