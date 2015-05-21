# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fixmybicycle', '0007_auto_20150521_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cyclist',
            options={},
        ),
        migrations.RemoveField(
            model_name='cyclist',
            name='mugshot',
        ),
        migrations.RemoveField(
            model_name='cyclist',
            name='privacy',
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='user',
            field=models.OneToOneField(related_name='cyclist_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
