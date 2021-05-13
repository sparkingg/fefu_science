from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
    UsernameField,
)
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

from .managers import UNIVERSITY_DOMAIN
from .models import UniversityUser


class UniversityUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UniversityUser
        fields = ("email", "first_name", "patronimic_name", "last_name", "department")


class UniversityUserChangeForm(UserChangeForm):
    class Meta:
        model = UniversityUser
        fields = ("email", "first_name", "patronimic_name", "last_name", "department")


class UniversityUserAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True}),
        validators=[
            RegexValidator(
                f"^.*(.{UNIVERSITY_DOMAIN})$",
                message=_("Email address must be a university email."),
            )
        ],
    )

    error_messages = {
        "invalid_login": _(
            "Enter a correct email and password. Both fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }
