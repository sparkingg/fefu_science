from django.utils.translation import gettext as _
from django_tables2 import Column

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, EmptyCRUDTable

from .models import Publication


class PublicationTable(EmptyCRUDTable):
    authors = Column(
        verbose_name=_("Authors"),
        accessor="get_authors",
        order_by=(
            "foreign_authors",
            "employee_authors",
            "postgraduate_authors",
            "student_authors",
        ),
    )
    crud_urls = Column(verbose_name="", accessor="get_crud_urls", orderable=False)

    class Meta:
        model = Publication
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = _(f"No publications have been added yet.")
        attrs = DEFAULT_ATTRS
