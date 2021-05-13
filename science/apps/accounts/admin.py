from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .forms import UniversityUserChangeForm, UniversityUserCreationForm
from .models import UniversityUser


class UniversityUserAdmin(UserAdmin):
    add_form = UniversityUserCreationForm
    form = UniversityUserChangeForm
    model = UniversityUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "department",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "first_name",
        "last_name",
        "department",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "patronimic_name",
                    "last_name",
                    "department",
                )
            },
        ),
        (_("Permissions"), {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name", "department")
    ordering = ("first_name", "last_name", "department")


admin.site.register(UniversityUser, UniversityUserAdmin)
