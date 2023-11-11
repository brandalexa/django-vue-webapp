from django.contrib import admin
from .models import Event

class APIAdmin(admin.ModelAdmin):
    list_display = ["description", "date"]

admin.site.register(Event, APIAdmin)
