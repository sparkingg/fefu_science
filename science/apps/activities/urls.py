from django.urls import path

from apps.activities import views
from apps.activities.models import Activity

urlpatterns = [
    path(
        "activity-table",
        views.ActivityTableView.as_view(),
        name="activities-activity-table",
    ),
    path(
        "activity-create",
        views.ActivityCreateView.as_view(),
        name="activities-activity-create",
    ),
    path(
        "activity-read/<int:pk>",
        views.ActivityReadView.as_view(),
        name="activities-activity-read",
    ),
    path(
        "activity-update/<int:pk>",
        views.ActivityUpdateView.as_view(),
        name="activities-activity-update",
    ),
    path(
        "activity-delete/<int:pk>",
        views.ActivityDeleteView.as_view(),
        name="activities-activity-delete",
    ),
]
