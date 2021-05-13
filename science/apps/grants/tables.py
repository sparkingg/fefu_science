from django_tables2.columns import Column
from sortedcontainers import SortedSet

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from .models import Grant
from .text import TABLES


class GrantTable(CRUDTable):
    time_period = Column(visible=False)
    financing = Column(visible=False)
    participants = Column(visible=False)
    postgraduates_number_payed = Column(visible=False)
    postgraduates_number = Column(visible=False)
    students_number_payed = Column(visible=False)
    students_number = Column(visible=False)

    def value_participants(self, value):
        participants = SortedSet(value)
        return ", ".join(participants)

    class Meta:
        model = Grant
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = TABLES.get("empty_text")
        attrs = DEFAULT_ATTRS
