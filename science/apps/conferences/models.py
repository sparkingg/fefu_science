from django.contrib.postgres.fields import ArrayField
from django.db import models
from sortedcontainers import SortedSet

from apps.common.models import AuthorField, NamedEntity
from crud.models import CRUDModel

from .text import FIELDS, MODELS


class ConferenceType(NamedEntity):
    NAME_FIELD_LENGTH = 100

    class Meta:
        verbose_name = MODELS.get("conference_type")
        verbose_name_plural = MODELS.get("conference_type_plural")


class Conference(CRUDModel):
    description = models.TextField(FIELDS.get("description"), unique=True)

    employee_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("employee_authors"),
        blank=True,
    )

    foreign_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("foreign_authors"),
        blank=True,
    )

    postgraduate_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("postgraduate_authors"),
        blank=True,
    )

    student_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("student_authors"),
        blank=True,
    )

    conference_type = models.ForeignKey(
        ConferenceType,
        on_delete=models.PROTECT,
        verbose_name=FIELDS.get("conference_type"),
    )

    date_added = models.DateField(FIELDS.get("date_added"), auto_now_add=True)

    def get_authors(self):
        authors = SortedSet(
            [
                *self.employee_authors,
                *self.foreign_authors,
                *self.postgraduate_authors,
                *self.student_authors,
            ]
        )
        return ", ".join(authors)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["description"]
        verbose_name = MODELS.get("conference")
        verbose_name_plural = MODELS.get("conferences")
