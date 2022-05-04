from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import MenuItem


class MenuItemAdmin(ModelAdmin):
    model = MenuItem
    menu_order = 296
    menu_label = _("Menu")
    list_display = [
        "name",
    ]


modeladmin_register(MenuItemAdmin)