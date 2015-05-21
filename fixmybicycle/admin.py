from django.contrib import admin
from .models import Cyclist,Bicycle,MaintenanceTask,Maintenance,Activity

# Register your models here.

#class CyclistAdmin(admin.ModelAdmin):
#    fieldsets = []


admin.site.register(Cyclist)
admin.site.register(Bicycle)
admin.site.register(MaintenanceTask)
admin.site.register(Maintenance)
admin.site.register(Activity)