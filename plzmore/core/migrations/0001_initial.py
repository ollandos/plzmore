# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plzid', models.SlugField(max_length=11, unique=True)),
            ],
        ),
    ]
