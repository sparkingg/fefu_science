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

from .forms import CollectionForm
from .models import Collection
from .tables import CollectionTable


class CollectionTableView(CRUDTableView):
    model = Collection
    table_class = CollectionTable
    template_name = "papers/collection_table.html"
    paginate_by = 15
    extra_context = {"title": _("Collections")}


class CollectionCreateView(BSModalCreateView):
    template_name = "papers/collection_create.html"
    form_class = CollectionForm
    success_message = _("Collection was created.")
    success_url = reverse_lazy(PathBuilder.build_table_path(Collection))


class CollectionReadView(BSModalReadView):
    model = Collection
    template_name = "papers/collection_read.html"


class CollectionUpdateView(BSModalUpdateView):
    model = Collection
    template_name = "papers/collection_update.html"
    form_class = CollectionForm
    success_message = _("Collection was updated.")
    success_url = reverse_lazy(PathBuilder.build_table_path(Collection))


class CollectionDeleteView(BSModalDeleteView):
    model = Collection
    template_name = "papers/collection_delete.html"
    success_message = _("Collection was deleted.")
    success_url = reverse_lazy(PathBuilder.build_table_path(Collection))
