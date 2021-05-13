from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _

from crud.models import CRUDModel


class NamedModel(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(NamedModel):
    code = models.CharField(
        _("Code"),
        unique=True,
        validators=[RegexValidator(r"^([\d]{2}){1}(.\1){0,2}$")],
        max_length=10,
    )
    name = models.CharField(_("Name"), max_length=150, unique=True)


class UniversityPriority(NamedModel):
    name = models.CharField(_("Name"), max_length=200, unique=True)


class ScientificPriority(NamedModel):
    name = models.CharField(_("Name"), max_length=200, unique=True)


class EconomicPriority(NamedModel):
    name = models.CharField(_("Name"), max_length=200, unique=True)


class CriticalTechnology(NamedModel):
    name = models.CharField(_("Name"), max_length=200, unique=True)


class StrategicDirection(NamedModel):
    name = models.CharField(_("Name"), max_length=250, unique=True)


class Research(CRUDModel):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    university_priority = models.ForeignKey(
        UniversityPriority,
        on_delete=models.CASCADE,
        verbose_name=_("University Priority"),
    )

    scientific_priority = models.ForeignKey(
        ScientificPriority,
        on_delete=models.CASCADE,
        verbose_name=_("Scientific Priority"),
    )

    critical_technology = models.ForeignKey(
        CriticalTechnology,
        on_delete=models.CASCADE,
        verbose_name=_("Critical Technology"),
    )

    economic_priority = models.ForeignKey(
        EconomicPriority, on_delete=models.CASCADE, verbose_name=_("Economic Priority"),
    )

    strategic_direction = models.ForeignKey(
        StrategicDirection,
        on_delete=models.CASCADE,
        verbose_name=_("Strategic Direction"),
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("CSCSTI")
    )

    academic_advisor = models.CharField(_("Academic Advisor"), max_length=50)

    reasons = models.TextField(_("Reason"))

    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Research")
        verbose_name_plural = _("Research")
