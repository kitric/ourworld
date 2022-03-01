from django.shortcuts import render, get_object_or_404
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

def eon_detail(request, eon_id):
    eon = get_object_or_404(models.GeoEon, id=eon_id)
    context = {
        'active_timescales': 'active',
        'eon': eon
    }
    return render(request, 'timescales/eon.html', context=context)

def era_detail(request, era_id):
    era = get_object_or_404(models.GeoEra, id=era_id)
    periods = era.periods.all()
    # using filters to avoid exceptions.
    next_era = models.GeoEra.objects.filter(id=era_id + 1).first()
    prev_era = models.GeoEra.objects.filter(id=era_id - 1).first()
    context = {
        'active_timescales': 'active',
        'era': era,
        'periods': periods,
        'next': next_era,
        'prev': prev_era
    }
    return render(request, 'timescales/era.html', context=context)

def period_detail(request, period_id):
    period = get_object_or_404(models.GeoPeriod, id=period_id)
    context = {
        'active_timescales': 'active',
        'period': period
    }
    return render(request, 'timescales/period.html', context=context)