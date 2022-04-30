from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import SiteSettings


@register(SiteSettings)
class SiteSettingsTranslation(TranslationOptions):
    fields = (
        "organization_name",
        "organization_tagline",
        "customer_service",
        "footer_links",
        "about_us_text",
        "copyright_text",
    )
