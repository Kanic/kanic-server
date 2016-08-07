# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetaMechanic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('is_certified', models.BooleanField(default=False)),
                ('certification', models.CharField(max_length=40, null=True, blank=True)),
                ('work_type', models.CharField(max_length=40, choices=[(b'FT', b'Full Time'), (b'PT', b'Part Time')])),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HiringJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resume', models.FileField(upload_to=b'upload/')),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'job title')),
                ('code', models.CharField(unique=True, max_length=255, verbose_name=b'job code')),
                ('requirement', models.CharField(max_length=3000, verbose_name=b'job requirements')),
                ('responsibility', models.CharField(max_length=3000, verbose_name=b'job responsibility')),
                ('description', models.CharField(max_length=3000, verbose_name=b'job description')),
                ('type', models.CharField(max_length=3000, verbose_name=b'job type')),
                ('salary', models.CharField(max_length=30, verbose_name=b'job salary')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('zipCode', models.CharField(max_length=7)),
                ('car', models.BooleanField(default=False)),
                ('createAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='hiringjob',
            name='job',
            field=models.ForeignKey(to='beta.Job'),
        ),
    ]
