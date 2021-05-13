from django.utils.translation import gettext as _

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from apps.activities.models import Activity
from apps.activities.text import TABLES


class ActivityTable(CRUDTable):
    class Meta:
        model = Activity
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = TABLES["empty_text"]
        attrs = DEFAULT_ATTRS
