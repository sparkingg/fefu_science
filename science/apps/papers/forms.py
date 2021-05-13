from bootstrap_modal_forms.forms import BSModalForm

from .models import Collection


class CollectionForm(BSModalForm):
    class Meta:
        model = Collection
        exclude = ("date_added",)
