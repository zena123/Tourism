from django.forms.utils import ErrorList
from wagtail.core import blocks
from django.utils.translation import ugettext_lazy as _
from wagtail.core.blocks.struct_block import StructBlockValidationError
from wagtail.images.blocks import ImageChooserBlock


class LinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255, help_text=_("Add link title"))
    external_url = blocks.CharBlock(required=False, help_text=_("Add External link or internal page only"))
    internal_page = blocks.PageChooserBlock(required=False, help_text=_("Add External link or internal page only"))

    def clean(self, value):
        errors = {}
        external_url = value.get("external_url", None)
        internal_page = value.get("internal_page", None)
        if external_url and internal_page:
            errors["external_url"] = ErrorList(
                [_("Both of these fields can't be filled . Please select one option.")]
            )
            errors["internal_page"] = ErrorList(
                [_("Both of these fields can't be filled . Please select one option.")]
            )

        if not external_url and not internal_page:
            errors["external_url"] = ErrorList(
                [_("Please select external link or internal page. ")]
            )
            errors["internal_page"] = ErrorList(
                [_("Please select external link or internal page.")]
            )

        if errors:
            raise StructBlockValidationError(errors)

        return super(LinkBlock, self).clean(value)


class BestTravelsBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255, help_text=_("Add title"))
    description = blocks.TextBlock(help_text=_("Add description"))
