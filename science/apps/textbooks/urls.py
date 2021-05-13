from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Guide, Manual, Textbook

urlpatterns = [
    path(
        "textbook-table",
        views.TextbookTableView.as_view(),
        name=PathBuilder.build_table_path(Textbook),
    ),
    path(
        "textbook-create",
        views.TextbookCreateView.as_view(),
        name=PathBuilder.build_create_path(Textbook),
    ),
    path(
        "textbook-read/<int:pk>",
        views.TextbookReadView.as_view(),
        name=PathBuilder.build_read_path(Textbook),
    ),
    path(
        "textbook-update/<int:pk>",
        views.TextbookUpdateView.as_view(),
        name=PathBuilder.build_update_path(Textbook),
    ),
    path(
        "textbook-delete/<int:pk>",
        views.TextbookDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Textbook),
    ),
    path(
        "manual-table",
        views.ManualTableView.as_view(),
        name=PathBuilder.build_table_path(Manual),
    ),
    path(
        "manual-create",
        views.ManualCreateView.as_view(),
        name=PathBuilder.build_create_path(Manual),
    ),
    path(
        "manual-read/<int:pk>",
        views.ManualReadView.as_view(),
        name=PathBuilder.build_read_path(Manual),
    ),
    path(
        "manual-update/<int:pk>",
        views.ManualUpdateView.as_view(),
        name=PathBuilder.build_update_path(Manual),
    ),
    path(
        "manual-delete/<int:pk>",
        views.ManualDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Manual),
    ),
    path(
        "guide-table",
        views.GuideTableView.as_view(),
        name=PathBuilder.build_table_path(Guide),
    ),
    path(
        "guide-create",
        views.GuideCreateView.as_view(),
        name=PathBuilder.build_create_path(Guide),
    ),
    path(
        "guide-read/<int:pk>",
        views.GuideReadView.as_view(),
        name=PathBuilder.build_read_path(Guide),
    ),
    path(
        "guide-update/<int:pk>",
        views.GuideUpdateView.as_view(),
        name=PathBuilder.build_update_path(Guide),
    ),
    path(
        "guide-delete/<int:pk>",
        views.GuideDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Guide),
    ),
]
