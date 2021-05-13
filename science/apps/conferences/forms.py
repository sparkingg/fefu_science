from collections import namedtuple

from bootstrap_modal_forms.forms import BSModalForm
from django.forms import ValidationError

from .models import Conference
from .text import ERRORS, FORMS

Authors = namedtuple(
    "Authors", ["employees", "foreigners", "postgraduates", "students"]
)


class ConferenceForm(BSModalForm):
    def _get_authors_cleaned(self):
        return Authors(
            self.cleaned_data.get("employee_authors"),
            self.cleaned_data.get("foreign_authors"),
            self.cleaned_data.get("postgraduate_authors"),
            self.cleaned_data.get("student_authors"),
        )

    def clean(self):
        super(ConferenceForm, self).clean()

        authors = self._get_authors_cleaned()
        if (
            not authors.employees
            and not authors.foreigners
            and not authors.postgraduates
            and not authors.students
        ):
            raise ValidationError(ERRORS.get("no_authors"))

    class Meta:
        model = Conference
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")
