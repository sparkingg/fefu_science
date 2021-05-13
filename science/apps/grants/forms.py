from bootstrap_modal_forms.forms import BSModalForm
from django.forms import ValidationError

from .models import Grant
from .text import ERRORS, FORMS


class GrantForm(BSModalForm):
    def _clean_number_of_participants(self, data):
        return data if data else 0

    def clean_postgraduates_number_payed(self):
        return self._clean_number_of_participants(
            self.cleaned_data["postgraduates_number_payed"]
        )

    def clean_postgraduates_number(self):
        return self._clean_number_of_participants(
            self.cleaned_data["postgraduates_number"]
        )

    def clean_students_number_payed(self):
        return self._clean_number_of_participants(
            self.cleaned_data["students_number_payed"]
        )

    def clean_students_number(self):
        return self._clean_number_of_participants(self.cleaned_data["students_number"])

    def _get_number_of_participants_cleaned(self):
        return (
            self.cleaned_data["postgraduates_number_payed"]
            + self.cleaned_data["postgraduates_number"]
            + self.cleaned_data["students_number_payed"]
            + self.cleaned_data["students_number"]
        )

    def clean(self):
        super(GrantForm, self).clean()

        number_of_student_authors = self._get_number_of_participants_cleaned()
        length_of_participants_list = len(self.cleaned_data["participants"])
        if number_of_student_authors != length_of_participants_list:
            raise ValidationError(ERRORS.get("incompatible_participants_values"))

    class Meta:
        model = Grant
        exclude = ("date_added",)
        help_texts = FORMS.get("help_texts")
        error_messages = FORMS.get("error_messages")
