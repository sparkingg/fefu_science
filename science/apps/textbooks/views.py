from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy

from crud.utils import PathBuilder
from crud.views import CRUDTableView

from .forms import GuideForm, ManualForm, TextbookForm
from .models import Guide, Manual, Textbook
from .tables import GuideTable, ManualTable, TextbookTable
from .text import FIELDS, TEMPLATES, VIEWS


class TextbookTableView(CRUDTableView):
    model = Textbook
    table_class = TextbookTable
    template_name = "textbooks/textbook/textbook_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table").get("textbook")}


class TextbookCreateView(BSModalCreateView):
    template_name = "textbooks/textbook/textbook_create.html"
    form_class = TextbookForm
    success_message = VIEWS.get("created").get("textbook")
    success_url = reverse_lazy(PathBuilder.build_table_path(Textbook))
    extra_context = {"title": TEMPLATES.get("create").get("textbook")}


class TextbookReadView(BSModalReadView):
    model = Textbook
    template_name = "textbooks/textbook/textbook_read.html"
    extra_context = {"title": TEMPLATES.get("read").get("textbook"), "fields": FIELDS}


class TextbookUpdateView(BSModalUpdateView):
    model = Textbook
    template_name = "textbooks/textbook/textbook_update.html"
    form_class = TextbookForm
    success_message = VIEWS.get("updated").get("textbook")
    success_url = reverse_lazy(PathBuilder.build_table_path(Textbook))
    extra_context = {"title": TEMPLATES.get("update").get("textbook")}


class TextbookDeleteView(BSModalDeleteView):
    model = Textbook
    template_name = "textbooks/textbook/textbook_delete.html"
    success_message = VIEWS.get("deleted").get("textbook")
    success_url = reverse_lazy(PathBuilder.build_table_path(Textbook))
    extra_context = {"title": TEMPLATES.get("delete").get("textbook")}


class ManualTableView(CRUDTableView):
    model = Manual
    table_class = ManualTable
    template_name = "textbooks/textbook/textbook_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table").get("manual")}


class ManualCreateView(BSModalCreateView):
    template_name = "textbooks/manual/manual_create.html"
    form_class = ManualForm
    success_message = VIEWS.get("created").get("manual")
    success_url = reverse_lazy(PathBuilder.build_table_path(Manual))
    extra_context = {"title": TEMPLATES.get("create").get("manual")}


class ManualReadView(BSModalReadView):
    model = Manual
    template_name = "textbooks/manual/manual_read.html"
    extra_context = {"title": TEMPLATES.get("read").get("manual"), "fields": FIELDS}


class ManualUpdateView(BSModalUpdateView):
    model = Manual
    template_name = "textbooks/manual/manual_update.html"
    form_class = ManualForm
    success_message = VIEWS.get("updated").get("manual")
    success_url = reverse_lazy(PathBuilder.build_table_path(Manual))
    extra_context = {"title": TEMPLATES.get("update").get("manual")}


class ManualDeleteView(BSModalDeleteView):
    model = Manual
    template_name = "textbooks/manual/manual_delete.html"
    success_message = VIEWS.get("deleted").get("manual")
    success_url = reverse_lazy(PathBuilder.build_table_path(Manual))
    extra_context = {"title": TEMPLATES.get("delete").get("manual")}


class GuideTableView(CRUDTableView):
    model = Guide
    table_class = GuideTable
    template_name = "textbooks/guide/guide_table.html"
    paginate_by = 15
    extra_context = {"title": TEMPLATES.get("table").get("guide")}


class GuideCreateView(BSModalCreateView):
    template_name = "textbooks/guide/guide_create.html"
    form_class = GuideForm
    success_message = VIEWS.get("created").get("guide")
    success_url = reverse_lazy(PathBuilder.build_table_path(Guide))
    extra_context = {"title": TEMPLATES.get("create").get("guide")}


class GuideReadView(BSModalReadView):
    model = Guide
    template_name = "textbooks/guide/guide_read.html"
    extra_context = {"title": TEMPLATES.get("read").get("guide"), "fields": FIELDS}


class GuideUpdateView(BSModalUpdateView):
    model = Guide
    template_name = "textbooks/guide/guide_update.html"
    form_class = GuideForm
    success_message = VIEWS.get("updated").get("guide")
    success_url = reverse_lazy(PathBuilder.build_table_path(Guide))
    extra_context = {"title": TEMPLATES.get("update").get("guide")}


class GuideDeleteView(BSModalDeleteView):
    model = Guide
    template_name = "textbooks/guide/guide_delete.html"
    success_message = VIEWS.get("deleted").get("guide")
    success_url = reverse_lazy(PathBuilder.build_table_path(Guide))
    extra_context = {"title": TEMPLATES.get("delete").get("guide")}
