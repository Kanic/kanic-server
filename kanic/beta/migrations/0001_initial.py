# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('zipCode', models.CharField(max_length=7)),
                ('car', models.BooleanField(default=False)),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
