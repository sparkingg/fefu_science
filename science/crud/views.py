from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin


class CRUDTableView(ExportMixin, SingleTableView):
    exclude_columns = ("crud_urls",)
    export_formats = ["csv", "xls"]
