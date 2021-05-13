from bootstrap_modal_forms.forms import BSModalForm

from .models import Research


class ResearchForm(BSModalForm):
    class Meta:
        model = Research
        exclude = ("date_added", "added_by")
