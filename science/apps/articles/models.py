from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from sortedcontainers import SortedSet

from apps.common.models import AuthorField, NamedEntity
from crud.models import CRUDModel


class PublicationType(NamedEntity):
    class Meta:
        verbose_name = _("Publication Type")
        verbose_name_plural = _("Publication Types")


class BibliographicDatabase(NamedEntity):
    class Meta:
        verbose_name = _("Bibliographic Database")
        verbose_name_plural = _("Bibliographic Databases")


class ArticleCategory(models.Model):
    name = models.CharField("Наименование", max_length=350)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория статьи"
        verbose_name_plural = "Категории статьи"


class Article(CRUDModel):
    description = models.TextField(_("Description"))

    publication_type = models.ForeignKey(
        PublicationType, on_delete=models.PROTECT, verbose_name=_("Publication Type")
    )

    impact = models.DecimalField(
        _("Impact Factor"),
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(0)],
    )

    employee_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Employee Authors"), blank=True,
    )

    foreign_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Foreign Authors"), blank=True,
    )

    postgraduate_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Postgraduate Authors"), blank=True,
    )

    student_authors = ArrayField(
        AuthorField(max_length=25), verbose_name=_("Student Authors"), blank=True,
    )

    bibliographic_databases = models.ManyToManyField(
        BibliographicDatabase,
        verbose_name=_("Bibliographic Database"),
        related_name="articles",
    )

    url = models.URLField(_("Link to Publication"))

    category = models.ForeignKey(
        ArticleCategory, on_delete=models.CASCADE, verbose_name="Категория"
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
        return f'{_("Article")} {self.id}'

    class Meta:
        ordering = ["description"]
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
