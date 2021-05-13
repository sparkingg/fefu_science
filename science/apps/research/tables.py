from django.utils.translation import gettext as _

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from .models import Research


class ResearchTable(CRUDTable):
    class Meta:
        model = Research
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = _("No research have been added yet.")
        attrs = DEFAULT_ATTRS
