from site_settings.models import SiteSettings


def global_context_processor(request):
    obj = SiteSettings.objects.first()

    return {
        "settings": obj or None
    }
