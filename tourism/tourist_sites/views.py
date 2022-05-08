from django.shortcuts import render
from django.views.generic import TemplateView


class TouristSitesView(TemplateView):
    template_name = 'tourist_sites/tourist_sites.html'
