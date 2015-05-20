from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Used to define the site user/athlete
class Cyclist(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    date_created = models.DateTimeField('date created')
    # no doubt need more stuff including login user

# each cyclist/athlete can have more than one bicycle!
class Bicycle(models.Model):
    cyclist = models.ForeignKey(Cyclist)
    make = models.CharField(max_length=300)
    model = models.CharField(max_length=300)

# This model defines the nature of a maintenance task you want to perform
# eg. On my Trek road bike I may want to change my chain every 3000km
# eg. On my Mountain bike I may want to check the headstem every 6 months
class MaintenanceTask(models.Model):

    DISTANCE = 1 # Every X km/m
    RIDING_TIME = 2 # Every x hours riding the bike
    CALENDAR_DAYS = 3 #Every x calendar days

    interval_type_choices = (
        (DISTANCE, 'Distance'),# Every X km/m
        (RIDING_TIME, 'Riding Time'),# Every x hours riding the bike
        (CALENDAR_DAYS, 'Calendar Days'),#Every x calendar days
    )

    bicycle = models.ForeignKey(Bicycle)
    name = models.CharField(max_length=100) #Name of maintenance task. eg Replace Chain
    description = models.CharField(max_length=500) #Additional descriptive information on nature of task
    interval = models.DecimalField(decimal_places=2, max_digits=10)
    interval_type = models.IntegerField(choices=interval_type_choices, default=DISTANCE)


# Model to store activity/ride information.
# Will be imported from Strava etc. This information is used to calculate
# WHEN each maintenance tasks is next needing to be done
class Activity(models.Model):
    cyclist = models.ForeignKey(Cyclist)
    bicycle = models.ForeignKey(Bicycle)
    start_time = models.DateTimeField('Date and Time of Activity start')
    end_time = models.DateTimeField('Date and Time of Activity end')
    distance = models.FloatField('Total distance of activity')
    moving_duration = models.IntegerField('Total moving time of activity in seconds')

# Model to store information of a maintenance task being completed at a certain time
# this will keep a record of the maintenance done on the bicycle
class Maintenance(models.Model):
    time_of_maintenance = models.DateTimeField()
    task_performed = models.ForeignKey(MaintenanceTask)



