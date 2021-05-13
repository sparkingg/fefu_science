from django_tables2.columns import Column

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from .models import Contest
from .text import TABLES


class ContestTable(CRUDTable):
    program = Column(visible=False)

    class Meta:
        model = Contest
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = TABLES.get("empty_text")
        attrs = DEFAULT_ATTRS
