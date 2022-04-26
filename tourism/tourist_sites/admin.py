from wagtail.contrib.modeladmin.options import (
    modeladmin_register,
    ModelAdminGroup,
    ModelAdmin,
)
from django.utils.translation import gettext_lazy as _
from .models import City, TouristPlace


class CityAdmin(ModelAdmin):
    model = City
    menu_label = _("Cities")
    list_display = ["name", ]


class TouristPlaceAdmin(ModelAdmin):
    model = TouristPlace
    menu_label = _("Tourist places")
    list_display = ["title", "show_in_home", ]


class TouristSitesGroupAdmin(ModelAdminGroup):
    menu_order = 294
    menu_label = _("Tourist Sites")
    items = (
        CityAdmin,
        TouristPlaceAdmin
    )


modeladmin_register(TouristSitesGroupAdmin)

