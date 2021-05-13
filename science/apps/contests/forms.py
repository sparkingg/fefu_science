from bootstrap_modal_forms.forms import BSModalForm

from .models import Contest
from .text import FORMS


class ContestForm(BSModalForm):
    class Meta:
        model = Contest
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")
