from django.contrib.auth import get_user_model
from django.test import TestCase

from appsaccounts.managers import UNIVERSITY_DOMAIN
from apps.common.models import Department


class TestUserManager(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.password = "foo"
        self.first_name = "Ivan"
        self.patronimic_name = "Ivanovich"
        self.last_name = "Ivanov"
        self.test_department = Department(name="Test")
        self.test_department.save()

    def test_corporate_email_required(self):
        email = "user@example.com"
        with self.assertRaises(ValueError):
            self.user_model.objects.create_user(
                email=email, password=self.password,
            )

    def test_create_user(self):
        normal_email = f"normal@{UNIVERSITY_DOMAIN}"

        user = self.user_model.objects.create_user(
            email=normal_email,
            password=self.password,
            first_name=self.first_name,
            patronimic_name=self.patronimic_name,
            last_name=self.last_name,
            department=self.test_department,
        )

        self.assertEqual(user.email, normal_email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            self.user_model.objects.create_user()
        with self.assertRaises(TypeError):
            self.user_model.objects.create_user(email="")
        with self.assertRaises(ValueError):
            self.user_model.objects.create_user(email="", password=self.password)

    def test_create_superuser(self):
        admin_email = f"super@{UNIVERSITY_DOMAIN}"

        admin_user = self.user_model.objects.create_superuser(
            email=admin_email,
            password=self.password,
            first_name=self.first_name,
            patronimic_name=self.patronimic_name,
            last_name=self.last_name,
            department=self.test_department,
        )

        self.assertEqual(admin_user.email, admin_email)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            # Username is `None` for the `AbstractUser` option.
            # Username does not exist for the `AbstractBaseUser` option.
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            self.user_model.objects.create_superuser(
                email=admin_email, password=self.password, is_superuser=False
            )
        with self.assertRaises(ValueError):
            self.user_model.objects.create_superuser(
                email=admin_email, password=self.password, is_staff=False
            )
