import itertools

import django_tables2 as tables
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django_tables2.columns import Column
from sortedcontainers import SortedSet


class ArticleTable(tables.Table):
    MAX_DESCRIPTION_LENGTH = 150

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count(1)

    description = tables.Column()

    number_of_foreign_authors = Column(
        verbose_name="Количество авторов (сотрудники)",
        accessor="foreign_authors",
        visible=False,
    )
    foreign_authors = Column(visible=False)

    number_of_employee_authors = Column(
        verbose_name="Количество авторов (иностранцы)",
        accessor="employee_authors",
        visible=False,
    )
    employee_authors = Column(visible=False)

    number_of_postgraduate_authors = Column(
        verbose_name="Количество авторов (аспиранты, докторанты)",
        accessor="postgraduate_authors",
        visible=False,
    )
    postgraduate_authors = Column(visible=False)

    number_of_student_authors = Column(
        verbose_name="Количество авторов (студенты)",
        accessor="student_authors",
        visible=False,
    )
    student_authors = Column(visible=False)

    category = Column(visible=False)

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

    crud_urls = tables.Column(
        verbose_name="",
        accessor="get_crud_urls",
        orderable=False,
        exclude_from_export=True,
    )

    def render_description(self, value):
        if len(value) < self.MAX_DESCRIPTION_LENGTH:
            return value
        return f"{value[:self.MAX_DESCRIPTION_LENGTH]}..."

    def _render_action_url(self, value, action_class, icon):
        return format_html(
            f"""
            <button type="button" class="{action_class} btn btn-sm btn-outline-primary"
                data-id="{value}">
                    <span data-feather={icon}></span>
            </button>
            """
        )

    def _render_read_url(self, value):
        return self._render_action_url(value, "read-article", "eye")

    def _render_update_url(self, value):
        return self._render_action_url(value, "update-article", "edit-3")

    def _render_delete_url(self, value):
        return self._render_action_url(value, "delete-article", "trash")

    def render_crud_urls(self, value):
        return format_html(
            f"""
            <div class="btn-group" role="group">
                {self._render_read_url(value.read)}
                {self._render_update_url(value.update)}
                {self._render_delete_url(value.delete)}
            </div>
            """
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
        template_name = "common/tables/bootstrap4.html"
        empty_text = _("No articles have been added yet.")
        attrs = {
            "thead": {"class": "thead-primary"},
            "th": {"class": "align-middle heading-sortable"},
            "td": {"class": "align-middle"},
        }
