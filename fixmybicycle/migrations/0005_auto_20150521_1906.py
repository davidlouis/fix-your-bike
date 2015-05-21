# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixmybicycle', '0004_auto_20150521_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='make',
            field=models.CharField(max_length=300, verbose_name=b'Make'),
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='model',
            field=models.CharField(max_length=300, verbose_name=b'Model'),
        ),
    ]
