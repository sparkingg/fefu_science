from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Collection

urlpatterns = [
    path(
        "collection-table",
        views.CollectionTableView.as_view(),
        name=PathBuilder.build_table_path(Collection),
    ),
    path(
        "collection-create",
        views.CollectionCreateView.as_view(),
        name=PathBuilder.build_create_path(Collection),
    ),
    path(
        "collection-read/<int:pk>",
        views.CollectionReadView.as_view(),
        name=PathBuilder.build_read_path(Collection),
    ),
    path(
        "collection-update/<int:pk>",
        views.CollectionUpdateView.as_view(),
        name=PathBuilder.build_update_path(Collection),
    ),
    path(
        "collection-delete/<int:pk>",
        views.CollectionDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Collection),
    ),
]
