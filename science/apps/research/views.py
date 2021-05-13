from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from crud.views import CRUDTableView

from .forms import ResearchForm
from .models import Research
from .tables import ResearchTable


class ResearchTableView(CRUDTableView):
    model = Research
    table_class = ResearchTable
    template_name = "research/research_table.html"
    paginate_by = 15
    extra_context = {"title": ngettext("Research", "Research", 2)}


class ResearchCreateView(BSModalCreateView):
    template_name = "research/research_create.html"
    form_class = ResearchForm
    success_message = _("Research was created.")
    success_url = reverse_lazy("research-research-table")


class ResearchReadView(BSModalReadView):
    model = Research
    template_name = "research/research_read.html"


class ResearchUpdateView(BSModalUpdateView):
    model = Research
    template_name = "research/research_update.html"
    form_class = ResearchForm
    success_message = _("Research was updated.")
    success_url = reverse_lazy("research-research-table")


class ResearchDeleteView(BSModalDeleteView):
    model = Research
    template_name = "research/research_delete.html"
    success_message = _("Research was deleted.")
    success_url = reverse_lazy("research-research-table")
