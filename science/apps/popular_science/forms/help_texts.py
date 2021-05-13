from django.utils.translation import gettext as _

AUTHOR_TEXT = _(
    'List authors according to the format of "Last Name FN.[MN.]." separated by commas.'
)

HELP_TEXTS = {
    "description": _("Enter a description of the publication without authors."),
    "employee_authors": AUTHOR_TEXT,
    "foreign_authors": AUTHOR_TEXT,
    "postgraduate_authors": AUTHOR_TEXT,
    "student_authors": AUTHOR_TEXT,
}


def get_help_texts():
    return HELP_TEXTS
