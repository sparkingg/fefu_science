from collections import namedtuple

from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.utils.translation import gettext as _

from .models import Guide, Manual, Textbook
from .text import FORMS

Authors = namedtuple(
    "Authors", ["employees", "foreigners", "postgraduates", "students"]
)


class BookForm(BSModalForm):
    def _get_authors_cleaned(self):
        return Authors(
            self.cleaned_data.get("employee_authors"),
            self.cleaned_data.get("foreign_authors"),
            self.cleaned_data.get("postgraduate_authors"),
            self.cleaned_data.get("student_authors"),
        )

    def clean(self):
        super(BookForm, self).clean()

        authors = self._get_authors_cleaned()
        if (
            not authors.employees
            and not authors.foreigners
            and not authors.postgraduates
            and not authors.students
        ):
            raise forms.ValidationError(_("Authors must be specified."))


class TextbookForm(BookForm):
    class Meta:
        model = Textbook
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")


class ManualForm(BookForm):
    class Meta:
        model = Manual
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")


class GuideForm(BookForm):
    class Meta:
        model = Guide
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")
