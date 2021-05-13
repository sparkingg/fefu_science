from django.db import models

from apps.common.models import AuthorField, NamedEntity

from apps.activities.text import FIELDS, MODELS


class ActivityType(models.Model):
    name = models.CharField(
        verbose_name=FIELDS["activity_type"]["name"], max_length=200,
    )
    date_added = models.DateTimeField(
        verbose_name=FIELDS["activity_type"]["date_added"],
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = MODELS["activity_type"]
        verbose_name_plural = MODELS["activity_type_plural"]

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(verbose_name=FIELDS["activity"]["name"], max_length=300,)
    participants = models.IntegerField(
        verbose_name=FIELDS["activity"]["participants"], blank=True, null=True
    )
    participants_university = models.IntegerField(
        verbose_name=FIELDS["activity"]["participants_university"],
        blank=True,
        null=True,
    )
    participants_foreign = models.IntegerField(
        verbose_name=FIELDS["activity"]["participants_foreign"], blank=True, null=True
    )
    participants_country = models.CharField(
        verbose_name=FIELDS["activity"]["participants_country"],
        max_length=50,
        blank=True,
        null=True,
    )
    financing_source = models.CharField(
        verbose_name=FIELDS["activity"]["financing_source"],
        max_length=300,
        blank=True,
        null=True,
    )
    financing_amount = models.FloatField(
        verbose_name=FIELDS["activity"]["financing_amount"], blank=True, null=True,
    )
    bibliographic_description = models.TextField(
        verbose_name=FIELDS["activity"]["bibliographic_description"],
        blank=True,
        null=True,
    )
    publications_url = models.URLField(
        verbose_name=FIELDS["activity"]["publications_url"], blank=True, null=True,
    )
    journal_name = models.CharField(
        verbose_name=FIELDS["activity"]["journal_name"],
        max_length=100,
        blank=True,
        null=True,
    )
    activity_type = models.ForeignKey(
        verbose_name=FIELDS["activity"]["activity_type"],
        to=ActivityType,
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(
        verbose_name=FIELDS["activity"]["date_added"],
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = "Научное мероприятие"
        verbose_name_plural = "Научные мероприятия"

    def __str__(self):
        return self.name
