from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import HomePage


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = (
        "home_banner",
        "home_data",
        "agents_opinions",
    )
