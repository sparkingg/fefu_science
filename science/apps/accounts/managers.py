from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

UNIVERSITY_DOMAIN = "dvfu.ru"


class UniversityUserManager(BaseUserManager):
    """
    Custom user model manager where a corporate university email is
    a unique identifier for authentication instead of a username.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("Email address is required."))
        if not email.endswith(UNIVERSITY_DOMAIN):
            raise ValueError(_("Email address must be a university email."))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have `is_staff=True`."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have `is_superuser=True`."))
        return self.create_user(email, password, **extra_fields)
