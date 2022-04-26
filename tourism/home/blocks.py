from wagtail.core import blocks
from django.utils.translation import ugettext_lazy as _
from wagtail.images.blocks import ImageChooserBlock


class BannerImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text=_("Add banner image"))


class HomeBannerBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255, help_text=_("Add Banner title"))
    description = blocks.TextBlock(help_text=_("Add  Banner description"))
    images = blocks.ListBlock(BannerImageBlock)


# add basic data to homepage
class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255, help_text=_("Add title"))
    description = blocks.TextBlock(help_text=_("Add  description"))
    icon = ImageChooserBlock(help_text=_("Add icon"))


class AgentBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255, help_text=_("Add agent name"))
    description = blocks.TextBlock(help_text=_("Add agent opinion"))
    avatar = ImageChooserBlock(help_text=_("Add avatar"))
    job = blocks.CharBlock(max_length=255, required=False)
