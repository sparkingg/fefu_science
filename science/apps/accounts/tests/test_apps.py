from django.test import TestCase
from django.utils.translation import gettext as _

from ..apps import AccountsConfig


class TestConfig(TestCase):
    def test_name(self):
        self.assertEquals(AccountsConfig.name, "accounts")

    def test_verbose_name(self):
        self.assertEquals(AccountsConfig.verbose_name, _("Accounts"))
