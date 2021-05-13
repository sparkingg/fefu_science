from django_tables2.columns import Column
from sortedcontainers import SortedSet

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from .models import Conference
from .text import TABLES


class ConferenceTable(CRUDTable):
    number_of_foreign_authors = Column(
        verbose_name=TABLES.get("number_of_foreign_authors"),
        accessor="foreign_authors",
        visible=False,
    )
    foreign_authors = Column(visible=False)

    number_of_employee_authors = Column(
        verbose_name=TABLES.get("number_of_employee_authors"),
        accessor="employee_authors",
        visible=False,
    )
    employee_authors = Column(visible=False)

    number_of_postgraduate_authors = Column(
        verbose_name=TABLES.get("number_of_postgraduate_authors"),
        accessor="postgraduate_authors",
        visible=False,
    )
    postgraduate_authors = Column(visible=False)

    number_of_student_authors = Column(
        verbose_name=TABLES.get("number_of_student_authors"),
        accessor="student_authors",
        visible=False,
    )
    student_authors = Column(visible=False)

    authors = Column(
        verbose_name="Авторы",
        accessor="get_authors",
        order_by=(
            "foreign_authors",
            "employee_authors",
            "postgraduate_authors",
            "student_authors",
        ),
        exclude_from_export=True,
    )

    def value_description(self, value, record):
        return f"{record.get_authors()} {value}"

    def _value_authors(self, value):
        authors = SortedSet(value)
        return ", ".join(authors)

    def value_foreign_authors(self, value):
        return self._value_authors(value)

    def value_employee_authors(self, value):
        return self._value_authors(value)

    def value_postgraduate_authors(self, value):
        return self._value_authors(value)

    def value_student_authors(self, value):
        return self._value_authors(value)

    def _value_number_of_authors(self, value):
        number_of_authors = len(value)
        return number_of_authors if number_of_authors > 0 else None

    def value_number_of_foreign_authors(self, value):
        return self._value_number_of_authors(value)

    def value_number_of_employee_authors(self, value):
        return self._value_number_of_authors(value)

    def value_number_of_postgraduate_authors(self, value):
        return self._value_number_of_authors(value)

    def value_number_of_student_authors(self, value):
        return self._value_number_of_authors(value)

    class Meta:
        model = Conference
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = (
            "description",
            "number_of_employee_authors",
            "employee_authors",
            "number_of_foreign_authors",
            "foreign_authors",
            "number_of_postgraduate_authors",
            "postgraduate_authors",
            "number_of_student_authors",
            "student_authors",
            "authors",
            "conference_type",
            "crud_urls",
        )
        empty_text = TABLES.get("empty_text")
        attrs = DEFAULT_ATTRS
