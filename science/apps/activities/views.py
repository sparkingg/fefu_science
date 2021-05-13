from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from apps.activities.forms import ActivityForm
from apps.activities.models import Activity
from apps.activities.tables import ActivityTable
from apps.activities.text import FIELDS, TEMPLATES, VIEWS


class ActivityTableView(CRUDTableView):
    model = Activity
    table_class = ActivityTable
    template_name = "activities/activity_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table")}


class ActivityCreateView(BSModalCreateView):
    template_name = "activities/activity_create.html"
    form_class = ActivityForm
    success_message = VIEWS.get("created")
    success_url = reverse_lazy("activities-activity-table")
    extra_context = {"title": TEMPLATES.get("create")}


class ActivityReadView(BSModalReadView):
    model = Activity
    template_name = "activities/activity_read.html"
    extra_context = {"title": TEMPLATES.get("read"), "fields": FIELDS}


class ActivityUpdateView(BSModalUpdateView):
    model = Activity
    template_name = "activities/activity_update.html"
    form_class = ActivityForm
    success_message = VIEWS.get("updated")
    success_url = reverse_lazy("activities-activity-table")
    extra_context = {"title": TEMPLATES.get("update")}


class ActivityDeleteView(BSModalDeleteView):
    model = Activity
    template_name = "activities/activity_delete.html"
    success_message = VIEWS.get("deleted")
    success_url = reverse_lazy("activities-activity-table")
    extra_context = {"title": TEMPLATES.get("delete")}
