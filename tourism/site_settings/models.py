from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    TabbedInterface,
    ObjectList,
)
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import FooterMenuBlock, CustomerServiceBlock


@register_setting
class SiteSettings(BaseSetting):
    organization_name = models.CharField(_("Organization Name"), max_length=100)
    organization_tagline = models.CharField(_("Organization tagline"), max_length=100)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        related_query_name="+",
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name=_("site_logo"),
    )
    logo_footer = models.ForeignKey(
        "wagtailimages.Image",
        related_query_name="+",
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name=_("footer_logo"),
    )
    customer_service = StreamField(
        [("CustomerServiceBlock", CustomerServiceBlock())], null=True, blank=True, block_counts={
            "CustomerServiceBlock": {"max_num": 1},
        },
    )
    footer_links = StreamField(
        [("FooterMenuBlock", FooterMenuBlock())], null=True, blank=True,
        block_counts={
            "FooterMenuBlock": {"max_num": 1}},

    )
    about_us_text = models.TextField(_("About us text"), null=True, blank=True)
    copyright_text = models.CharField(_("Copyright Text"), max_length=255, default=_("All rights reserved"))

    panels = [
        TabbedInterface(
            [
                ObjectList(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel("organization_name"),
                                FieldPanel("organization_tagline"),
                                ImageChooserPanel("logo"),
                                ImageChooserPanel("logo_footer"),
                                FieldPanel("about_us_text"),
                            ],

                            heading=_("General Site Settings"),
                        )
                    ],
                    heading=_("General Settings"),
                ),
                ObjectList(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel("copyright_text"),
                                StreamFieldPanel("footer_links"),

                            ], heading=_("Footer Settings"),
                        )
                    ],
                    heading=_("Footer"),
                ),
                ObjectList(
                    [
                        MultiFieldPanel(
                            [
                                StreamFieldPanel("customer_service"),
                            ],
                            heading=_("Customer Service "),
                        )
                    ],
                    heading=_("Customer Services"),
                ),
            ]
        )
    ]

    # TODO:en/ar later
    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")
