from collections import namedtuple

from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.utils.translation import gettext as _

from ..models import Publication
from .error_messages import get_error_messages
from .help_texts import get_help_texts

Authors = namedtuple(
    "Authors", ["employees", "foreigners", "postgraduates", "students"]
)


class PublicationForm(BSModalForm):
    def _get_authors_cleaned(self):
        return Authors(
            self.cleaned_data.get("employee_authors"),
            self.cleaned_data.get("foreign_authors"),
            self.cleaned_data.get("postgraduate_authors"),
            self.cleaned_data.get("student_authors"),
        )

    def clean(self):
        super(PublicationForm, self).clean()

        authors = self._get_authors_cleaned()
        if (
            not authors.employees
            and not authors.foreigners
            and not authors.postgraduates
            and not authors.students
        ):
            raise forms.ValidationError(_("Authors must be specified."))

    class Meta:
        model = Publication
        exclude = ("date_added",)
        help_texts = get_help_texts()
        error_messages = get_error_messages()
