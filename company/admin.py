from django.contrib import admin
from .models import Company
from .models import Change
from .models import Trademark
from .models import Classification


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'province', 'city', 'district', 'company_type', 'operating_status')
    list_filter = ('province', )
    search_fields = ('name', 'industry', 'company_type', 'operating_status')


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('company', 'change_date', 'change_item', 'before_change', 'after_change', 'create_date')
    list_filter = ('create_date', 'change_date')
    # date_hierarchy = 'change_date'
    search_fields = ('company__name', 'change_item')


@admin.register(Trademark)
class TrademarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('trademark', 'classification', 'process', 'status')
    list_filter = ('classification', 'process', 'status')
    search_fields = ('trademark__name', )
