from django.urls import path

from . import views

urlpatterns = [
    path(
        "article-table", views.ArticleTableView.as_view(), name="articles-article-table"
    ),
    path(
        "article-create",
        views.ArticleCreateView.as_view(),
        name="articles-article-create",
    ),
    path(
        "article-read/<int:pk>",
        views.ArticleReadView.as_view(),
        name="articles-article-read",
    ),
    path(
        "article-update/<int:pk>",
        views.ArticleUpdateView.as_view(),
        name="articles-article-update",
    ),
    path(
        "article-delete/<int:pk>",
        views.ArticleDeleteView.as_view(),
        name="articles-article-delete",
    ),
]
