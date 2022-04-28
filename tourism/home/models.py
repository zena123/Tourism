from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import MultiFieldPanel, StreamFieldPanel
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
