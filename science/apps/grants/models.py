from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import AuthorField
from crud.models import CRUDModel

from .text import FIELDS, MODELS


class Grant(CRUDModel):
    fond = models.CharField(FIELDS.get("fond"), max_length=150)

    contest = models.CharField(FIELDS.get("contest"), max_length=250)

    project = models.CharField(FIELDS.get("project"), max_length=300, unique=True)

    time_period = models.CharField(FIELDS.get("time_period"), max_length=50)

    financing = models.CharField(FIELDS.get("financing"), max_length=50)

    manager = models.CharField(FIELDS.get("manager"), max_length=100)

    participants = ArrayField(
        AuthorField(max_length=25), verbose_name=FIELDS.get("participants"),
    )

    postgraduates_number_payed = models.IntegerField(
        FIELDS.get("postgraduates_number_payed"),
        validators=[MinValueValidator(0)],
        blank=True,
    )

    postgraduates_number = models.IntegerField(
        FIELDS.get("postgraduates_number"),
        validators=[MinValueValidator(0)],
        blank=True,
    )

    students_number_payed = models.IntegerField(
        FIELDS.get("students_number_payed"),
        validators=[MinValueValidator(0)],
        blank=True,
    )

    students_number = models.IntegerField(
        FIELDS.get("students_number"), validators=[MinValueValidator(0)], blank=True
    )

    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project

    class Meta:
        ordering = ["fond"]
        verbose_name = MODELS.get("grant").get("singular")
        verbose_name_plural = MODELS.get("grant").get("plural")
