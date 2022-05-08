from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City


class TouristSitesView(ListView):
    model = City
    template_name = 'tourist_sites/tourist_sites.html'

