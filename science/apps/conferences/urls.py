from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Conference

urlpatterns = [
    path(
        "conference-table",
        views.ConferenceTableView.as_view(),
        name=PathBuilder.build_table_path(Conference),
    ),
    path(
        "conference-create",
        views.ConferenceCreateView.as_view(),
        name=PathBuilder.build_create_path(Conference),
    ),
    path(
        "conference-read/<int:pk>",
        views.ConferenceReadView.as_view(),
        name=PathBuilder.build_read_path(Conference),
    ),
    path(
        "conference-update/<int:pk>",
        views.ConferenceUpdateView.as_view(),
        name=PathBuilder.build_update_path(Conference),
    ),
    path(
        "conference-delete/<int:pk>",
        views.ConferenceDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Conference),
    ),
]
