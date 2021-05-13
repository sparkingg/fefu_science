from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from .forms import PublicationForm
from .models import Publication
from .tables import PublicationTable


class PublicationTableView(CRUDTableView):
    model = Publication
    table_class = PublicationTable
    template_name = "popular_science/publication_table.html"
    paginate_by = 15
    extra_context = {"title": _("Publications")}


class PublicationCreateView(BSModalCreateView):
    template_name = "popular_science/publication_create.html"
    form_class = PublicationForm
    success_message = _("Publication was created.")
    success_url = reverse_lazy(PathBuilder.build_table_path(Publication))


class PublicationReadView(BSModalReadView):
    model = Publication
    template_name = "popular_science/publication_read.html"


class PublicationUpdateView(BSModalUpdateView):
    model = Publication
    template_name = "popular_science/publication_update.html"
    form_class = PublicationForm
    success_message = _("Publication was updated.")
    success_url = reverse_lazy(PathBuilder.build_table_path(Publication))


class PublicationDeleteView(BSModalDeleteView):
    model = Publication
    template_name = "popular_science/publication_delete.html"
    success_message = _("Publication was deleted.")
    success_url = reverse_lazy(PathBuilder.build_table_path(Publication))
