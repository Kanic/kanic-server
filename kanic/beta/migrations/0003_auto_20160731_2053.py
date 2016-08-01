# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0002_betamechanic'),
    ]

    operations = [
        migrations.AddField(
            model_name='tester',
            name='first_name',
            field=models.CharField(default='ahmed', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tester',
            name='last_name',
            field=models.CharField(default='bens', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='betamechanic',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='betamechanic',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tester',
            name='name',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
