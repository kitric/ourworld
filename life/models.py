from django.db import models
from timescales.models import GeoPeriod

# Create your models here.
class Species(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField()
    characteristics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    summary = models.TextField()
    website = models.URLField(max_length=500)

    def __str__(self):
        return self.name
        
class Organism(models.Model):
    ORGANISM_TYPES = [
        ("AN", "Animal"),
        ("PL", "Plant"),
        ("BA", "Bacteria"),
        ("FU", "Fungi")
    ]

    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    organism_type = models.CharField(max_length=3, choices=ORGANISM_TYPES)
    period = models.ForeignKey(GeoPeriod, on_delete=models.SET_NULL, blank=True, null=True)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, blank=True, null=True)
    endangered = models.BooleanField(default=False)
    habitat = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    extent = models.CharField(max_length=50, blank=True, null=True)
    image_primary = models.URLField(max_length=500, blank=True, null=True)
    image_secondary = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name