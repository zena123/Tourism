from site_settings.models import SiteSettings
from home.models import MenuItem


def global_context_processor(request):
    obj = SiteSettings.objects.first()
    menu = MenuItem.objects.all()

    return {
        "settings": obj or None,
        "menu_items": menu or None
    }
