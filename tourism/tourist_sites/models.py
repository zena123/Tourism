from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class City(models.Model):
    name = models.CharField(_("City Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    panels = [
        FieldPanel("name"),
    ]


class TouristPlace(ClusterableModel):
    title = models.CharField(_("Title"), max_length=255)
    intro_text = models.TextField(_("Introduction Text"))
    description = RichTextField(_("Description"))
    show_in_home = models.BooleanField(_("Show in home"), default=False)

    def __str__(self):
        return self.title

    panels = [
        FieldPanel("title"),
        FieldPanel("intro_text"),
        FieldPanel("description"),
        FieldPanel("show_in_home"),
        InlinePanel("tourist_images", heading=_("Related site images"), min_num=1),
    ]

    @property
    def image(self):
        return (
            self.tourist_images.first().image if self.tourist_images.exists() else None
        )


class TouristPlaceImages(Orderable):
    tourist_place = ParentalKey(
        TouristPlace, on_delete=models.CASCADE, related_name="tourist_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        related_query_name="+",
        on_delete=models.CASCADE,
        verbose_name=_("Image"),
    )

    panels = [
        ImageChooserPanel("image"),
    ]
