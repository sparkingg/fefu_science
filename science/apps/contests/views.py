from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from .forms import ContestForm
from .models import Contest
from .tables import ContestTable
from .text import FIELDS, TEMPLATES, VIEWS


class ContestTableView(CRUDTableView):
    model = Contest
    table_class = ContestTable
    template_name = "contests/contest_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table")}


class ContestCreateView(BSModalCreateView):
    template_name = "contests/contest_create.html"
    form_class = ContestForm
    success_message = VIEWS.get("created")
    success_url = reverse_lazy(PathBuilder.build_table_path(Contest))
    extra_context = {"title": TEMPLATES.get("create")}


class ContestReadView(BSModalReadView):
    model = Contest
    template_name = "contests/contest_read.html"
    extra_context = {"title": TEMPLATES.get("read"), "fields": FIELDS}


class ContestUpdateView(BSModalUpdateView):
    model = Contest
    template_name = "contests/contest_update.html"
    form_class = ContestForm
    success_message = VIEWS.get("updated")
    success_url = reverse_lazy(PathBuilder.build_table_path(Contest))
    extra_context = {"title": TEMPLATES.get("update")}


class ContestDeleteView(BSModalDeleteView):
    model = Contest
    template_name = "contests/contest_delete.html"
    success_message = VIEWS.get("deleted")
    success_url = reverse_lazy(PathBuilder.build_table_path(Contest))
    extra_context = {"title": TEMPLATES.get("delete")}
