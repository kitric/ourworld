from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='organisms'),
    path('<int:organism_id>/', views.organism, name='organism_detail'),
]