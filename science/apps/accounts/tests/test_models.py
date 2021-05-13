from django.test import TestCase
from django.utils import timezone

from ..managers import UNIVERSITY_DOMAIN
from ..models import UniversityUser

USER_DATA = {
    "email": f"user@{UNIVERSITY_DOMAIN}",
    "password": "foo",
}


def get_datetime_without_ms(datetime):
    return (
        datetime.year,
        datetime.month,
        datetime.day,
        datetime.hour,
        datetime.minute,
        datetime.second,
    )


class TestUser(TestCase):
    def setUp(self):
        self.user_basic = UniversityUser.objects.create(
            email=USER_DATA.get("email"), password=USER_DATA.get("password")
        )

    def test_email_is_set(self):
        self.assertEquals(self.user_basic.email, USER_DATA.get("email"))

    def test_email_is_username(self):
        self.assertEquals(self.user_basic.get_username(), USER_DATA.get("email"))

    def test_password_is_set(self):
        self.assertEquals(self.user_basic.password, USER_DATA.get("password"))

    def test_default_field_values(self):
        self.assertEquals(self.user_basic.first_name, "")
        self.assertEquals(self.user_basic.patronimic_name, "")
        self.assertEquals(self.user_basic.last_name, "")
        self.assertEquals(self.user_basic.department, None)
        self.assertEquals(self.user_basic.is_staff, False)
        self.assertEquals(self.user_basic.is_active, True)
        self.assertEquals(
            get_datetime_without_ms(self.user_basic.date_joined),
            get_datetime_without_ms(timezone.now()),
        )

    def test_string_representation(self):
        self.assertEquals(str(self.user_basic), USER_DATA.get("email"))
