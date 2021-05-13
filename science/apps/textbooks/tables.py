from django_tables2 import Column
from sortedcontainers import SortedSet

from apps.common.text import TABLES as COMMON_TABLES
from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, EmptyCRUDTable

from .models import Guide, Manual, Textbook
from .text import TABLES


class BookTable(EmptyCRUDTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    publisher = Column(visible=False)
    circulation = Column(visible=False)
    isbn = Column(visible=False)
    volume = Column(visible=False)
    volume_employees = Column(visible=False)
    field_of_study = Column(visible=False)
    category = Column(visible=False)

    number_of_foreign_authors = Column(
        verbose_name=COMMON_TABLES.get("number_of_foreign_authors"),
        accessor="foreign_authors",
        visible=False,
    )
    foreign_authors = Column(visible=False)

    number_of_employee_authors = Column(
        verbose_name=COMMON_TABLES.get("number_of_employee_authors"),
        accessor="employee_authors",
        visible=False,
    )
    employee_authors = Column(visible=False)

    number_of_postgraduate_authors = Column(
        verbose_name=COMMON_TABLES.get("number_of_postgraduate_authors"),
        accessor="postgraduate_authors",
        visible=False,
    )
    postgraduate_authors = Column(visible=False)

    number_of_student_authors = Column(
        verbose_name=COMMON_TABLES.get("number_of_student_authors"),
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

    crud_urls = Column(
        verbose_name="",
        accessor="get_crud_urls",
        orderable=False,
        exclude_from_export=True,
    )

    def render_circulation(self, value):
        if not value:
            return "Электронный ресурс"
        return value

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


class TextbookTable(BookTable):
    class Meta:
        model = Textbook
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = (
            "description",
            "...",
            "crud_urls",
        )
        attrs = DEFAULT_ATTRS
        empty_text = TABLES.get("empty_text").get("textbook")


class ManualTable(BookTable):
    class Meta:
        model = Manual
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = (
            "description",
            "...",
            "crud_urls",
        )
        attrs = DEFAULT_ATTRS
        empty_text = TABLES.get("empty_text").get("manual")


class GuideTable(BookTable):
    class Meta:
        model = Guide
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = (
            "description",
            "...",
            "crud_urls",
        )
        attrs = DEFAULT_ATTRS
        empty_text = TABLES.get("empty_text").get("guide")
