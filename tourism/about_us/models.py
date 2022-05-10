from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from home.blocks import AgentBlock, CardBlock
from .blocks import LinkBlock, BestTravelsBlock


class AboutUS(Page):
    max_count = 1
    template = 'about_us/about_us.html'

    main_content = StreamField(
        [("MainContent", CardBlock())],
        block_counts={
            "MainContent": {"max_num": 1},
        },
        null=True,
        blank=True,
    )

    principle = StreamField(
        [("PrincipleBlock", LinkBlock())],
        null=True,
        blank=True,
    )

    our_team = StreamField(
        [("OurTeamBlock", AgentBlock())],
        null=True,
        blank=True,
    )
    best_travel = StreamField(
        [("BestTravelBlock", BestTravelsBlock())],
        block_counts={
            "BestTravelBlock": {"max_num": 1},
        },
        null=True,
        blank=True,
    )
    public_relation = StreamField(
        [("BestTravelBlock", BestTravelsBlock())],
        block_counts={
            "BestTravelBlock": {"max_num": 1},
        },
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                StreamFieldPanel("main_content"),
            ],
            heading=_("Main Content Section"),
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("principle"),
            ],
            heading=_("principle Section"),
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("best_travel"),
            ],
            heading=_("Best travel Section"),
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("public_relation"),
            ],
            heading=_("Public relation Section"),
            classname="collapsible collapsed",
        ),
    ]




