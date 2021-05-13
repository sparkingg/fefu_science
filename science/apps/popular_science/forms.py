from bootstrap_modal_forms.forms import BSModalForm

from .models import Publication


class PublicationForm(BSModalForm):
    class Meta:
        model = Publication
        exclude = ("date_added",)
