# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fixmybicycle', '0006_auto_20150521_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyclist',
            name='user',
            field=models.OneToOneField(related_name='my_profile', verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
