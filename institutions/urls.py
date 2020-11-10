from django.urls import path

from . import views

urlpatterns = [
    path('', views.institutions_home, name="institutions_index_page"),
]