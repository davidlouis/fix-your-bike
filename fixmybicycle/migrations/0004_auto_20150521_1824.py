# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixmybicycle', '0003_auto_20150521_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='name',
            field=models.CharField(default='', max_length=300, verbose_name=b'Bicycle Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='make',
            field=models.CharField(max_length=300, verbose_name=b'The make of the bicycles'),
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='model',
            field=models.CharField(max_length=300, verbose_name=b'The model of the bicycle'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='task_performed',
            field=models.ForeignKey(verbose_name=b'The task performed', to='fixmybicycle.MaintenanceTask'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='time_of_maintenance',
            field=models.DateTimeField(verbose_name=b'Date and Time when maintenance task is performed'),
        ),
    ]
