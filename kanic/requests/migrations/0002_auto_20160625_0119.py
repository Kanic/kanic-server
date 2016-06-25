# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='createAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='request',
            name='lastModified',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='createAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='service',
            name='lastModified',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 25, 1, 19, 6, 849181, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
