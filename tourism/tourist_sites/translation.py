from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import City, TouristPlace


@register(City)
class CityTranslation(TranslationOptions):
    fields = (
        "name",
    )


@register(TouristPlace)
class TouristPlaceTranslation(TranslationOptions):
    fields = (
        "title",
        "intro_text",
        "description",
    )
