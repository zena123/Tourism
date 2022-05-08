from django.urls import path
from .views import TouristSitesView

app_name = "tourist_sites"

urlpatterns = [
    path("", TouristSitesView.as_view(), name="index"),
]
