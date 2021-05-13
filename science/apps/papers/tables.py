from django.utils.translation import gettext as _

from crud.tables import DEFAULT_ATTRS, DEFAULT_TEMPLATE, CRUDTable

from .models import Collection


class CollectionTable(CRUDTable):
    class Meta:
        model = Collection
        template_name = DEFAULT_TEMPLATE
        exclude = ("date_added",)
        sequence = ("...", "crud_urls")
        empty_text = _("No collections have been added yet.")
        attrs = DEFAULT_ATTRS
