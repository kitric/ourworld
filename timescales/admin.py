from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.GeoEon)
admin.site.register(models.GeoEra)
admin.site.register(models.GeoPeriod)