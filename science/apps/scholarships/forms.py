from bootstrap_modal_forms.forms import BSModalForm

from .models import Scholarship
from .text import FORMS


class ScholarshipForm(BSModalForm):
    class Meta:
        model = Scholarship
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")
