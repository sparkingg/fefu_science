from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import UniversityUserAuthenticationForm

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            form_class=UniversityUserAuthenticationForm,
        ),
        name="accounts-login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="accounts-logout",
    ),
]
