"""Views module for the Institutions app"""

from django.shortcuts import render


# Create your views here.

def institutions_home(request):
    """Institutions Home Page View Function"""
    return render(request, 'home/institutions_home.html', {})
