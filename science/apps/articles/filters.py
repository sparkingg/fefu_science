import django_filters as filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import Article, BibliographicDatabase, PublicationType


class ArticleFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr="icontains", label=_("Description"))

    publication_type__name = filters.ModelChoiceFilter(
        queryset=PublicationType.objects.all(), label=_("Publication Type")
    )

    impact__gt = filters.NumberFilter(
        field_name="impact", lookup_expr="gt", label=_("From")
    )

    impact__lt = filters.NumberFilter(
        field_name="impact", lookup_expr="lt", label=_("To")
    )

    authors = filters.CharFilter(method="filter_authors", label=_("Authors"))

    def filter_authors(self, queryset, name, value):
        return queryset.filter(
            Q(employee_authors__icontains=value)
            | Q(foreign_authors__icontains=value)
            | Q(postgraduate_authors__icontains=value)
            | Q(student_authors__icontains=value)
        )

    bibliographic_databases__name = filters.ModelChoiceFilter(
        queryset=BibliographicDatabase.objects.all(), label=_("Bibliographic Database")
    )

    class Meta:
        model = Article
        fields = ()
