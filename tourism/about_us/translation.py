from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import AboutUS


@register(AboutUS)
class AboutUSTranslation(TranslationOptions):
    fields = (
        "main_content",
        "principle",
        "our_team",
        "best_travel",
        "public_relation",
    )

