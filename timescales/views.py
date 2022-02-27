from django.shortcuts import render
from . import models

# Create your views here.
def timescales(request):
    geoeons = models.GeoEon.objects.all().order_by('absolute_number')
    geoeras = models.GeoEra.objects.all().order_by('absolute_number')
    geoperiods = models.GeoPeriod.objects.all().order_by('absolute_number')
    context = {
        'active_timescales': 'active',
        'geo_eons': geoeons,
        'geo_eras': geoeras,
        'geo_periods': geoperiods
    }
    return render(request, 'timescales/index.html', context=context)