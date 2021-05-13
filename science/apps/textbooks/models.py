from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from sortedcontainers import SortedSet

from apps.common.models import AuthorField, ISBNField
from crud.models import CRUDModel

from .text import FIELDS, MODELS


class FieldOfStudy(models.Model):
    name = models.CharField(FIELDS.get("name"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = MODELS.get("field_of_study").get("singular")
        verbose_name_plural = MODELS.get("field_of_study").get("plural")


class Book(CRUDModel):
    description = models.TextField(FIELDS.get("description"))

    publisher = models.CharField(
        FIELDS.get("publisher"), max_length=100, blank=True, null=True
    )

    circulation = models.IntegerField(
        FIELDS.get("circulation"),
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )

    isbn = ISBNField(FIELDS.get("isbn"), max_length=25, blank=True, null=True)

    field_of_study = models.ForeignKey(
        FieldOfStudy,
        on_delete=models.CASCADE,
        verbose_name=FIELDS.get("field_of_study"),
        blank=True,
        null=True,
    )

    volume = models.DecimalField(
        FIELDS.get("volume"),
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )

    volume_employees = models.DecimalField(
        FIELDS.get("volume_employees"),
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )

    employee_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("employee_authors"),
        blank=True,
        null=True,
    )

    foreign_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("foreign_authors"),
        blank=True,
        null=True,
    )

    postgraduate_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("postgraduate_authors"),
        blank=True,
        null=True,
    )

    student_authors = ArrayField(
        AuthorField(max_length=25),
        verbose_name=FIELDS.get("student_authors"),
        blank=True,
        null=True,
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
        abstract = True


class Category(models.Model):
    name = models.CharField(FIELDS.get("name"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class TextbookCategory(Category):
    class Meta:
        verbose_name = MODELS.get("textbook_category").get("singular")
        verbose_name_plural = MODELS.get("textbook_category").get("plural")


class Textbook(Book):
    category = models.ForeignKey(
        TextbookCategory, on_delete=models.CASCADE, verbose_name=FIELDS.get("category")
    )

    class Meta:
        verbose_name = MODELS.get("textbook").get("singular")
        verbose_name_plural = MODELS.get("textbook").get("plural")


class ManualCategory(Category):
    class Meta:
        verbose_name = MODELS.get("manual_category").get("singular")
        verbose_name_plural = MODELS.get("manual_category").get("plural")


class Manual(Book):
    category = models.ForeignKey(
        ManualCategory, on_delete=models.CASCADE, verbose_name=FIELDS.get("category")
    )

    class Meta:
        verbose_name = MODELS.get("manual").get("singular")
        verbose_name_plural = MODELS.get("manual").get("plural")


class GuideCategory(Category):
    class Meta:
        verbose_name = MODELS.get("guide_category").get("singular")
        verbose_name_plural = MODELS.get("guide_category").get("plural")


class Guide(Book):
    category = models.ForeignKey(
        GuideCategory, on_delete=models.CASCADE, verbose_name=FIELDS.get("category")
    )

    class Meta:
        ordering = ["description"]
        verbose_name = MODELS.get("guide").get("singular")
        verbose_name_plural = MODELS.get("guide").get("plural")
