from django_tables2.columns import Column
from sortedcontainers import SortedSet

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from .models import Scholarship
from .text import TABLES


class ScholarshipTable(CRUDTable):
    activity = Column(visible=False)

    def render_participants(self, value):
        participants = SortedSet(value)
        return ", ".join(participants)

    class Meta:
        model = Scholarship
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = TABLES.get("empty_text")
        attrs = DEFAULT_ATTRS
