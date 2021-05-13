import django_tables2 as tables
from django.utils.html import format_html

CRUD_ICONS = {"read": "eye", "update": "edit-3", "delete": "trash"}
DEFAULT_TEMPLATE = "common/tables/bootstrap4.html"
DEFAULT_ATTRS = {
    "th": {"class": "align-middle heading-sortable"},
    "td": {"class": "align-middle"},
}


class EmptyCRUDTable(tables.Table):
    """
    CRUD-model without any fields. CRUD-actions field
    must be defined manually.
    """

    def _render_action_url(self, value, action):
        model_name = (self._meta.model.__name__).lower()

        return format_html(
            f"""
            <button class="{action}-{model_name} btn btn-sm btn-outline-primary"
                type="button" data-id="{value}">
                    <span data-feather={CRUD_ICONS.get(action)}></span>
            </button>
            """
        )

    def _render_read_url(self, value):
        return self._render_action_url(value, "read")

    def _render_update_url(self, value):
        return self._render_action_url(value, "update")

    def _render_delete_url(self, value):
        return self._render_action_url(value, "delete")

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


class CRUDTable(EmptyCRUDTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    crud_urls = tables.Column(
        verbose_name="", accessor="get_crud_urls", orderable=False
    )
