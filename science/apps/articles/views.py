from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin

from .forms import ArticleForm
from .models import Article
from .tables import ArticleTable


class ArticleTableView(ExportMixin, SingleTableView):
    model = Article
    table_class = ArticleTable
    template_name = "articles/article_table.html"
    paginate_by = 15
    extra_context = {"title": _("Articles")}
    exclude_columns = ("crud_urls",)
    export_formats = ["csv", "xls"]
    export_name = "Scientific Articles"


class ArticleCreateView(BSModalCreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleForm
    success_message = _("Article was created.")
    success_url = reverse_lazy("articles-article-table")


class ArticleReadView(BSModalReadView):
    model = Article
    template_name = "articles/article_read.html"


class ArticleUpdateView(BSModalUpdateView):
    model = Article
    template_name = "articles/article_update.html"
    form_class = ArticleForm
    success_message = _("Article was updated.")
    success_url = reverse_lazy("articles-article-table")


class ArticleDeleteView(BSModalDeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_message = _("Article was deleted.")
    success_url = reverse_lazy("articles-article-table")
