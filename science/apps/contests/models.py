from django.db import models

from crud.models import CRUDModel

from .text import FIELDS, MODELS


class Contest(CRUDModel):
    fond = models.CharField(FIELDS.get("fond"), max_length=50)

    program = models.CharField(FIELDS.get("program"), max_length=200, blank=True)

    contest = models.CharField(FIELDS.get("contest"), max_length=300)

    project = models.CharField(FIELDS.get("project"), max_length=300, unique=True)

    manager = models.CharField(FIELDS.get("manager"), max_length=100)

    date_added = models.DateField(FIELDS.get("date_added"), auto_now_add=True)

    def __str__(self):
        return self.project

    class Meta:
        ordering = ["fond"]
        verbose_name = MODELS.get("contest").get("singular")
        verbose_name_plural = MODELS.get("contest").get("plural")
