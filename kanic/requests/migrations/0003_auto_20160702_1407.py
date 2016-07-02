# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20160625_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='car',
            field=models.ForeignKey(blank=True, to='cars.Model', null=True),
        ),
    ]
