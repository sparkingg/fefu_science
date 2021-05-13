from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Research

urlpatterns = [
    path(
        "research-table",
        views.ResearchTableView.as_view(),
        name=PathBuilder.build_table_path(Research),
    ),
    path(
        "research-create",
        views.ResearchCreateView.as_view(),
        name=PathBuilder.build_create_path(Research),
    ),
    path(
        "research-read/<int:pk>",
        views.ResearchReadView.as_view(),
        name=PathBuilder.build_read_path(Research),
    ),
    path(
        "research-update/<int:pk>",
        views.ResearchUpdateView.as_view(),
        name=PathBuilder.build_update_path(Research),
    ),
    path(
        "research-delete/<int:pk>",
        views.ResearchDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Research),
    ),
]
