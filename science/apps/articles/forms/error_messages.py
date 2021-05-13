from django.utils.translation import gettext as _

INVALID_ITEM_MESSAGE = _("Author %(nth)s does not conform to the format.")

ERROR_MESSAGES = {
    "employee_authors": {"item_invalid": INVALID_ITEM_MESSAGE},
    "foreign_authors": {"item_invalid": INVALID_ITEM_MESSAGE},
    "postgraduate_authors": {"item_invalid": INVALID_ITEM_MESSAGE},
    "student_authors": {"item_invalid": INVALID_ITEM_MESSAGE},
}


def get_error_messages():
    return ERROR_MESSAGES
