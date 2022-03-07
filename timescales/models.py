from django.db import models

# Create your models here.
class GeoPeriod(models.Model):
    name = models.CharField(max_length=50)
    extent_mya = models.IntegerField(default=0)
    duration_moy = models.IntegerField(default=0)
    absolute_number = models.IntegerField(default=0, unique=True)
    period_order_number = models.IntegerField(default=0)
    summary = models.TextField()
    life = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class GeoEra(models.Model):
    name = models.CharField(max_length=50)
    periods = models.ManyToManyField(GeoPeriod, blank=True)
    absolute_number = models.IntegerField(default=0, unique=True)
    era_order_number = models.IntegerField(default=0)
    summary = models.TextField()
    life = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class GeoEon(models.Model):
    name = models.CharField(max_length=50)
    eras = models.ManyToManyField(GeoEra, blank=True)
    absolute_number = models.IntegerField(default=0, unique=True)
    summary = models.TextField()
    life = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name