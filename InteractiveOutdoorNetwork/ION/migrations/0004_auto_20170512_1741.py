# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 00:41
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('ION', '0003_auto_20170512_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=django_markdown.models.MarkdownField(max_length=1000),
        ),
    ]
