from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import MultiFieldPanel, StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from .blocks import CardBlock, AgentBlock
from tourist_sites.models import TouristPlace


class HomePage(Page):
    max_count = 1
    template = 'home/home_page.html'

    home_banner = StreamField(
        [("BannerBlock", CardBlock())],
        block_counts={
            "BannerBlock": {"max_num": 3},
        },
        null=True,
        blank=True,
    )

    home_data = StreamField(
        [("HomeDataBlock", CardBlock())],
        null=True,
        blank=True,
    )

    agents_opinions = StreamField(
        [("AgentsBlock", AgentBlock())],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                StreamFieldPanel("home_banner"),
            ],
            heading=_("Home banner Section"),
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("home_data"),
            ],
            heading=_("Home data Section"),
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("agents_opinions"),
            ],
            heading=_("Agent data Section"),
            classname="collapsible collapsed",
        )
    ]

    def get_context(self, request, *args, **kwargs):
        ctx = super(HomePage, self).get_context(request, *args, **kwargs)
        ctx["places"] = TouristPlace.objects.filter(show_in_home=True)
        return ctx


class MenuItem(models.Model):
    name = models.CharField(_("Menu Item name"), max_length=250)
    external_link = models.URLField(_("External Url"), null=True, blank=True)
    internal_page = models.ForeignKey(
        "wagtailcore.Page",
        related_query_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("Page"),
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("external_link"),
        FieldPanel("internal_page"),
    ]

    def clean(self):

        if self.internal_page and self.external_link:
            raise ValidationError(
                _("Please select external link or internal page only.")
            )
        if not self.external_link and not self.internal_page:
            raise ValidationError(
                _("Please select external link or internal page only.")
            )