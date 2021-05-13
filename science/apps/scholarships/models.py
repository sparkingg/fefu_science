from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import AuthorField
from crud.models import CRUDModel

from .text import FIELDS, MODELS


class ScholarshipCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = MODELS.get("scholarship_category").get("singular")
        verbose_name_plural = MODELS.get("scholarship_category").get("plural")


class Scholarship(CRUDModel):
    fond = models.CharField(FIELDS.get("fond"), max_length=150)

    activity = models.CharField(FIELDS.get("activity"), max_length=250, blank=True)

    project = models.CharField(FIELDS.get("project"), max_length=300, blank=True)

    time_period = models.CharField(FIELDS.get("time_period"), max_length=50, blank=True)

    financing = models.IntegerField(
        FIELDS.get("financing"), validators=[MinValueValidator(0)]
    )

    participants = ArrayField(
        AuthorField(max_length=25), verbose_name=FIELDS.get("participants"),
    )

    support_type = models.CharField(FIELDS.get("support_type"), max_length=100)

    category = models.ForeignKey(
        ScholarshipCategory,
        on_delete=models.CASCADE,
        verbose_name=FIELDS.get("category"),
    )

    date_added = models.DateField(FIELDS.get("date_added"), auto_now_add=True)

    def __str__(self):
        return self.project

    class Meta:
        ordering = ["category"]
        verbose_name = MODELS.get("scholarship").get("singular")
        verbose_name_plural = MODELS.get("scholarship").get("plural")
