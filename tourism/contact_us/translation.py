from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import ContactUs


@register(ContactUs)
class ContactUsTranslation(TranslationOptions):
    fields = ()
