# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='make',
            name='niceName',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
