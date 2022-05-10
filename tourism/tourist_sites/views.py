from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import City, TouristPlace


class TouristSitesView(ListView):
    model = City
    template_name = 'tourist_sites/tourist_sites.html'


class TouristSiteDetail(DetailView):
    model = TouristPlace
    template_name = 'tourist_sites/tourist_site_detail.html'

