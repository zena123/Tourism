from django.urls import path
from .views import TouristSitesView, TouristSiteDetail

app_name = "tourist_sites"

urlpatterns = [
    path("", TouristSitesView.as_view(), name="index"),
    path("site-details/<int:pk>", TouristSiteDetail.as_view(), name="site-details"),
]
