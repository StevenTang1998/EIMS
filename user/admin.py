from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'tel']
    list_display = ('name', 'email', 'tel', 'belong')
    search_fields = ['name', 'belong__name']
