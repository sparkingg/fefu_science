from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import ISBNField
from crud.models import CRUDModel


class Collection(CRUDModel):
    description = models.TextField(_("Description"))

    publisher = models.CharField(_("Publisher"), max_length=100)

    isbn = ISBNField(_("ISBN"), max_length=25)

    edition = models.IntegerField(_("Edition"), validators=[MinValueValidator(0)])

    volume = models.DecimalField(
        _("Volume"), max_digits=6, decimal_places=3, validators=[MinValueValidator(0)]
    )

    volume_employees = models.DecimalField(
        _("Volume (Full-time university employees)"),
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(0)],
    )

    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["description"]
        verbose_name = _("Collection")
        verbose_name_plural = _("Collections")
