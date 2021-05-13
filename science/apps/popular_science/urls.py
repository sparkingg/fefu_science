from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Publication

urlpatterns = [
    path(
        "publication-table",
        views.PublicationTableView.as_view(),
        name=PathBuilder.build_table_path(Publication),
    ),
    path(
        "publication-create",
        views.PublicationCreateView.as_view(),
        name=PathBuilder.build_create_path(Publication),
    ),
    path(
        "publication-read/<int:pk>",
        views.PublicationReadView.as_view(),
        name=PathBuilder.build_read_path(Publication),
    ),
    path(
        "publication-update/<int:pk>",
        views.PublicationUpdateView.as_view(),
        name=PathBuilder.build_update_path(Publication),
    ),
    path(
        "publication-delete/<int:pk>",
        views.PublicationDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Publication),
    ),
]
