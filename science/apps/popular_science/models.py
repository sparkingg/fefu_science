from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext as _
from sortedcontainers import SortedSet

from apps.common.models import AuthorField
from crud.models import CRUDModel


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Field of Study")
        verbose_name_plural = _("Fields of Study")


class Publication(CRUDModel):
    description = models.TextField(_("Description"))
    field_of_study = models.ForeignKey(
        FieldOfStudy, on_delete=models.CASCADE, verbose_name=_("Field of Study")
    )
    employee_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Employee Authors"), blank=True
    )
    foreign_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Foreign Authors"), blank=True
    )
    postgraduate_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Postgraduate Authors"), blank=True
    )
    student_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Student Authors"), blank=True
    )
    date_added = models.DateField(auto_now_add=True)

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
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")
