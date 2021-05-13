from django.contrib import admin

from .models import (
    FieldOfStudy,
    Guide,
    GuideCategory,
    Manual,
    ManualCategory,
    Textbook,
    TextbookCategory,
)

admin.site.register(FieldOfStudy)
admin.site.register(Guide)
admin.site.register(GuideCategory)
admin.site.register(Manual)
admin.site.register(ManualCategory)
admin.site.register(Textbook)
admin.site.register(TextbookCategory)
