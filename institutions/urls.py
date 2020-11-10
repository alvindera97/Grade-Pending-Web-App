from django.urls import path

from institutions.views import institutions_home as home

urlpatterns = [
    path('', home),
]