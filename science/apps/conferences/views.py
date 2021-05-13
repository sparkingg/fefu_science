from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from .forms import ConferenceForm
from .models import Conference
from .tables import ConferenceTable
from .text import FIELDS, TEMPLATES, VIEWS


class ConferenceTableView(CRUDTableView):
    model = Conference
    table_class = ConferenceTable
    template_name = "conferences/conference_table.html"
    paginate_by = 15
    export_name = "Conferences"
    extra_context = {"title": TEMPLATES.get("table")}


class ConferenceCreateView(BSModalCreateView):
    template_name = "conferences/conference_create.html"
    form_class = ConferenceForm
    success_message = VIEWS.get("created")
    success_url = reverse_lazy(PathBuilder.build_table_path(Conference))
    extra_context = {"title": TEMPLATES.get("create")}


class ConferenceReadView(BSModalReadView):
    model = Conference
    template_name = "conferences/conference_read.html"
    extra_context = {"title": TEMPLATES.get("read"), "fields": FIELDS}


class ConferenceUpdateView(BSModalUpdateView):
    model = Conference
    template_name = "conferences/conference_update.html"
    form_class = ConferenceForm
    success_message = VIEWS.get("updated")
    success_url = reverse_lazy(PathBuilder.build_table_path(Conference))
    extra_context = {"title": TEMPLATES.get("update")}


class ConferenceDeleteView(BSModalDeleteView):
    model = Conference
    template_name = "conferences/conference_delete.html"
    success_message = VIEWS.get("deleted")
    success_url = reverse_lazy(PathBuilder.build_table_path(Conference))
    extra_context = {"title": TEMPLATES.get("delete")}
