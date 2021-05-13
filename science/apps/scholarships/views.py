from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from .forms import ScholarshipForm
from .models import Scholarship
from .tables import ScholarshipTable
from .text import FIELDS, TEMPLATES, VIEWS


class ScholarshipTableView(CRUDTableView):
    model = Scholarship
    table_class = ScholarshipTable
    template_name = "scholarships/scholarship_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table")}


class ScholarshipCreateView(BSModalCreateView):
    template_name = "scholarships/scholarship_create.html"
    form_class = ScholarshipForm
    success_message = VIEWS.get("created")
    success_url = reverse_lazy(PathBuilder.build_table_path(Scholarship))
    extra_context = {"title": TEMPLATES.get("create")}


class ScholarshipReadView(BSModalReadView):
    model = Scholarship
    template_name = "scholarships/scholarship_read.html"
    extra_context = {"title": TEMPLATES.get("read"), "fields": FIELDS}


class ScholarshipUpdateView(BSModalUpdateView):
    model = Scholarship
    template_name = "scholarships/scholarship_update.html"
    form_class = ScholarshipForm
    success_message = VIEWS.get("updated")
    success_url = reverse_lazy(PathBuilder.build_table_path(Scholarship))
    extra_context = {"title": TEMPLATES.get("update")}


class ScholarshipDeleteView(BSModalDeleteView):
    model = Scholarship
    template_name = "scholarships/scholarship_delete.html"
    success_message = VIEWS.get("deleted")
    success_url = reverse_lazy(PathBuilder.build_table_path(Scholarship))
    extra_context = {"title": TEMPLATES.get("delete")}
