from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.organisms, name='organisms')
]