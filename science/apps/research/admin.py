from django.contrib import admin

from .models import (
    Category,
    CriticalTechnology,
    EconomicPriority,
    Research,
    ScientificPriority,
    StrategicDirection,
    UniversityPriority,
)

admin.site.register(Category)
admin.site.register(CriticalTechnology)
admin.site.register(EconomicPriority)
admin.site.register(Research)
admin.site.register(ScientificPriority)
admin.site.register(StrategicDirection)
admin.site.register(UniversityPriority)
