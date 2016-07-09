# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='type',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='tools',
        ),
        migrations.AddField(
            model_name='service',
            name='detail',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='part',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
