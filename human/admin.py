from django.contrib import admin
from .models import Serving


@admin.register(Serving)
class ServingAdmin(admin.ModelAdmin):
    list_display = ('human_name', 'company', 'position')
    search_fields = ('human_name', 'company__name', 'position')
