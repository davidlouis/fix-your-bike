# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(verbose_name=b'Date and Time of Activity start')),
                ('end_time', models.DateTimeField(verbose_name=b'Date and Time of Activity end')),
                ('distance', models.FloatField(verbose_name=b'Total distance of activity')),
                ('moving_duration', models.IntegerField(verbose_name=b'Total moving time of activity in seconds')),
            ],
        ),
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make', models.CharField(max_length=300)),
                ('model', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cyclist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_of_maintenance', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('interval', models.DecimalField(max_digits=10, decimal_places=2)),
                ('interval_type', models.IntegerField(default=1, choices=[(1, b'Distance'), (2, b'Riding Time'), (3, b'Calendar Days')])),
                ('bicycle', models.ForeignKey(to='fixmybicycle.Bicycle')),
            ],
        ),
        migrations.AddField(
            model_name='maintenance',
            name='task_performed',
            field=models.ForeignKey(to='fixmybicycle.MaintenanceTask'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='cyclist',
            field=models.ForeignKey(to='fixmybicycle.Cyclist'),
        ),
        migrations.AddField(
            model_name='activity',
            name='bicycle',
            field=models.ForeignKey(to='fixmybicycle.Bicycle'),
        ),
        migrations.AddField(
            model_name='activity',
            name='cyclist',
            field=models.ForeignKey(to='fixmybicycle.Cyclist'),
        ),
    ]
