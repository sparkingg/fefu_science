from django.apps import AppConfig
from django.utils.translation import gettext as _


class AccountsConfig(AppConfig):
    name = "accounts"
    verbose_name = _("Accounts")
