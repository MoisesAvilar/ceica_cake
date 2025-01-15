from django.contrib import admin
from cashflow.models import Cashflow


@admin.register(Cashflow)
class CashflowAdmin(admin.ModelAdmin):
    list_display = ('value', 'category', 'date', 'created_at', 'updated_at', 'value_type', 'description')
