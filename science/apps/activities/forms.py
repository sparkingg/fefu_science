from bootstrap_modal_forms.forms import BSModalForm

from apps.activities.models import Activity


class ActivityForm(BSModalForm):
    class Meta:
        model = Activity
        exclude = ("date_added",)
