# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0004_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiringJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'job title')),
                ('resume', models.FileField(upload_to=b'upload/')),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
