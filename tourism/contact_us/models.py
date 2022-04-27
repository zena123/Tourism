from django.db import models
from django.conf import settings
from modelcluster.fields import ParentalKey
from django.utils import translation
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from django.utils.translation import ugettext_lazy as _


class TranslatedField:
    """ translation for wagtail form builder fields
            note that those fields will be generated in admin interface
    """
    def __init__(self,
                 en_field,
                 ar_field
                 ):
        self.en_field = en_field
        self.ar_field = ar_field

    def __get__(self, instance, owner):
        lang = translation.get_language()
        if lang == 'ar':
            return getattr(instance, self.ar_field)
        else:
            return getattr(instance, self.en_field)


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactUs", on_delete=models.CASCADE, related_name="custom_form_fields"
    )
    label_en = models.CharField(max_length=250, null=True, blank=True)
    label_ar = models.CharField(max_length=250, null=True, blank=True)
    label = TranslatedField(
        'label_en',
        'label_ar',
    )
    AbstractFormField.panels.remove(next((x for x in AbstractFormField.panels if x.field_name == 'label'), None))
    panels = AbstractFormField.panels + [
        FieldPanel('label_en'),
        FieldPanel('label_ar'),
    ]


class ContactUs(AbstractEmailForm):
    max_count = 1

    content_panels = AbstractEmailForm.content_panels + [

        InlinePanel("custom_form_fields", label=_("Form fields")),
        MultiFieldPanel(
            [
                FieldPanel("to_address"),
                FieldPanel("subject"),
            ],
            _("Email Configuration"),
        ),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()

