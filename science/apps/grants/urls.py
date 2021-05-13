from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Grant

urlpatterns = [
    path(
        "grant-table",
        views.GrantTableView.as_view(),
        name=PathBuilder.build_table_path(Grant),
    ),
    path(
        "grant-create",
        views.GrantCreateView.as_view(),
        name=PathBuilder.build_create_path(Grant),
    ),
    path(
        "grant-read/<int:pk>",
        views.GrantReadView.as_view(),
        name=PathBuilder.build_read_path(Grant),
    ),
    path(
        "grant-update/<int:pk>",
        views.GrantUpdateView.as_view(),
        name=PathBuilder.build_update_path(Grant),
    ),
    path(
        "grant-delete/<int:pk>",
        views.GrantDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Grant),
    ),
]
