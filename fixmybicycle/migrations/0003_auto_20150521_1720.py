# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixmybicycle', '0002_cyclist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name=b'Activity Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='date_created',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='maintenancetask',
            name='description',
            field=models.TextField(verbose_name=b'Addition description of task to be performed'),
        ),
    ]
