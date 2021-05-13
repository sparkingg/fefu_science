from django.contrib.auth.views import LoginView, LogoutView
from django.test import TestCase
from django.urls import resolve, reverse


class TestUrls(TestCase):
    def test_login_url_is_resolved(self):
        url = reverse("accounts-login")
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse("accounts-logout")
        self.assertEquals(resolve(url).func.view_class, LogoutView)
