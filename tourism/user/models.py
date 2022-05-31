from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="profiles",
        unique=True,
    )
    INTERESTS = (
        ("a", _("advertisement")),
        ("b", _("investing")),
        ("c", _("Staying in touch")),
    )
    interests = CharField(_("Interests"), max_length=50, choices=INTERESTS)
    is_publisher = models.BooleanField(_("Publisher"), default=False)
    dob = models.DateField(_("Date of birth"), null=True, blank=True)

    def __str__(self):
        full_name = "%s %s %s" % (self.first_name, self.middle_name, self.last_name,)
        return full_name.strip()
