from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Contest

urlpatterns = [
    path(
        "contest-table",
        views.ContestTableView.as_view(),
        name=PathBuilder.build_table_path(Contest),
    ),
    path(
        "contest-create",
        views.ContestCreateView.as_view(),
        name=PathBuilder.build_create_path(Contest),
    ),
    path(
        "contest-read/<int:pk>",
        views.ContestReadView.as_view(),
        name=PathBuilder.build_read_path(Contest),
    ),
    path(
        "contest-update/<int:pk>",
        views.ContestUpdateView.as_view(),
        name=PathBuilder.build_update_path(Contest),
    ),
    path(
        "contest-delete/<int:pk>",
        views.ContestDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Contest),
    ),
]
