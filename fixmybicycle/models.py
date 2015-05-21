from django.db import models

class Cyclist(models.Model):
    # Model used to define the site user/athlete
    user = models.OneToOneField('auth.User', related_name='cyclist_profile')
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    date_created = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    # no doubt need more stuff including login user

class Bicycle(models.Model):
    # each cyclist/athlete can have more than one bicycle!
    cyclist = models.ForeignKey(Cyclist)
    name = models.CharField(max_length=300, verbose_name='Bicycle Name')
    make = models.CharField(max_length=300, verbose_name='Make')
    model = models.CharField(max_length=300, verbose_name='Model')

    def __str__(self):
        return self.cyclist.first_name + ' ' + self.cyclist.last_name + ' (' +self.name + ')'

class MaintenanceTask(models.Model):
    # This model defines the nature of a maintenance task you want to perform
    # eg. On my Trek road bike I may want to change my chain every 3000km
    # eg. On my Mountain bike I may want to check the headstem every 6 months

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
    description = models.TextField(verbose_name='Addition description of task to be performed') #Additional descriptive information on nature of task
    interval = models.DecimalField(decimal_places=2, max_digits=10)
    interval_type = models.IntegerField(choices=interval_type_choices, default=DISTANCE)

    def __str__(self):
        return self.name

class Activity(models.Model):
    # Model to store activity/ride information.
    # Will be imported from Strava etc. This information is used to calculate
    # WHEN each maintenance tasks is next needing to be done
    name = models.CharField(max_length=100,verbose_name='Activity Name')
    cyclist = models.ForeignKey(Cyclist)
    bicycle = models.ForeignKey(Bicycle)
    start_time = models.DateTimeField(verbose_name='Date and Time of Activity start')
    end_time = models.DateTimeField(verbose_name='Date and Time of Activity end')
    distance = models.FloatField(verbose_name='Total distance of activity')
    moving_duration = models.IntegerField(verbose_name='Total moving time of activity in seconds')

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    # Model to store information of a maintenance task being completed at a certain time
    # this will keep a record of the maintenance done on the bicycle
    time_of_maintenance = models.DateTimeField(verbose_name='Date and Time when maintenance task is performed')
    task_performed = models.ForeignKey(MaintenanceTask, verbose_name='The task performed')

    def __str__(self):
        return 'Maintenance task: ' + self.task_performed.name + ' at ' + self.time_of_maintenance.__str__()
