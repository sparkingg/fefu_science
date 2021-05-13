from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _


class NamedEntity(models.Model):
    NAME_FIELD_LENGTH = 75

    name = models.CharField(_("Name"), max_length=NAME_FIELD_LENGTH)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Department(NamedEntity):
    NAME_FIELD_LENGTH = 100

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class AuthorField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(
            RegexValidator(r"^([a-zA-Zа-яА-Я ]*)(?<! ) ([A-ZА-Я]{1}.){1,2}$")
        )


class ISBNField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(
            RegexValidator(
                r"^(?:ISBN(?:-1[03])?:? )?(?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}$|97[89][0-9]{10}$|(?=(?:[0-9]+[- ]){4})[- 0-9]{17}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]$"
            )
        )
