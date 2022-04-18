from django.contrib import admin
from .models import Species, PointOfInterest, Organism

# Register your models here.
admin.site.register(Species)
admin.site.register(PointOfInterest)
admin.site.register(Organism)