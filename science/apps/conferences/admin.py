from django.contrib import admin

from .models import Conference, ConferenceType

admin.site.register(Conference)
admin.site.register(ConferenceType)
