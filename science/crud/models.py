from django.db import models
from django.urls import reverse_lazy

from .utils import Actions, PathBuilder


class CRUDModel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_url = PathBuilder.build_create_path(self.__class__)
        self.read_url = PathBuilder.build_read_path(self.__class__)
        self.update_url = PathBuilder.build_update_path(self.__class__)
        self.delete_url = PathBuilder.build_delete_path(self.__class__)

    def get_create_url(self):
        return reverse_lazy(self.create_url)

    def get_read_url(self):
        return reverse_lazy(self.read_url, kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy(self.update_url, kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy(self.delete_url, kwargs={"pk": self.pk})

    def get_crud_urls(self):
        return Actions(
            self.get_create_url(),
            self.get_read_url(),
            self.get_update_url(),
            self.get_delete_url(),
        )

    class Meta:
        abstract = True
