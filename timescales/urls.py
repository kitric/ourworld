from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.timescales, name='timescales'),
    path('eons/<int:eon_id>/', views.eon_detail, name='eon'),
    path('eras/<int:era_id>/', views.era_detail, name='era'),
    path('periods/<int:period_id>/', views.period_detail, name='period')
]