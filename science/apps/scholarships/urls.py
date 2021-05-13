from django.urls import path

from crud.utils import PathBuilder

from . import views
from .models import Scholarship

urlpatterns = [
    path(
        "scholarship-table",
        views.ScholarshipTableView.as_view(),
        name=PathBuilder.build_table_path(Scholarship),
    ),
    path(
        "scholarship-create",
        views.ScholarshipCreateView.as_view(),
        name=PathBuilder.build_create_path(Scholarship),
    ),
    path(
        "scholarship-read/<int:pk>",
        views.ScholarshipReadView.as_view(),
        name=PathBuilder.build_read_path(Scholarship),
    ),
    path(
        "scholarship-update/<int:pk>",
        views.ScholarshipUpdateView.as_view(),
        name=PathBuilder.build_update_path(Scholarship),
    ),
    path(
        "scholarship-delete/<int:pk>",
        views.ScholarshipDeleteView.as_view(),
        name=PathBuilder.build_delete_path(Scholarship),
    ),
]
