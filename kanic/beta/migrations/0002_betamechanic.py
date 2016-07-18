# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetaMechanic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('is_certified', models.BooleanField(default=False)),
                ('certification', models.CharField(max_length=40, null=True, blank=True)),
                ('work_type', models.CharField(max_length=40, choices=[(b'FT', b'Full Time'), (b'PT', b'Part Time')])),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
