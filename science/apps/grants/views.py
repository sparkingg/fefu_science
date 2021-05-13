from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from .forms import GrantForm
from .models import Grant
from .tables import GrantTable
from .text import FIELDS, TEMPLATES, VIEWS


class GrantTableView(CRUDTableView):
    model = Grant
    table_class = GrantTable
    template_name = "grants/grant_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table")}
    export_name = "Grants"


class GrantCreateView(BSModalCreateView):
    template_name = "grants/grant_create.html"
    form_class = GrantForm
    success_message = VIEWS.get("created")
    success_url = reverse_lazy(PathBuilder.build_table_path(Grant))
    extra_context = {"title": TEMPLATES.get("create")}


class GrantReadView(BSModalReadView):
    model = Grant
    template_name = "grants/grant_read.html"
    extra_context = {"title": TEMPLATES.get("read"), "fields": FIELDS}


class GrantUpdateView(BSModalUpdateView):
    model = Grant
    template_name = "grants/grant_update.html"
    form_class = GrantForm
    success_message = VIEWS.get("updated")
    success_url = reverse_lazy(PathBuilder.build_table_path(Grant))
    extra_context = {"title": TEMPLATES.get("update")}


class GrantDeleteView(BSModalDeleteView):
    model = Grant
    template_name = "grants/grant_delete.html"
    success_message = VIEWS.get("deleted")
    success_url = reverse_lazy(PathBuilder.build_table_path(Grant))
    extra_context = {"title": TEMPLATES.get("delete")}
