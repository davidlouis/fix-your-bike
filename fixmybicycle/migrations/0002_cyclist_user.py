# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fixmybicycle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cyclist',
            name='user',
            field=models.OneToOneField(related_name='cyclist_profile', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
