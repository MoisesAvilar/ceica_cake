from django.contrib import admin
from sales.models import Sale


@admin.register(Sale)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'quantity', 'total_sale', 'customer', 'data_hour', 'payment_status',
    )
    list_filter = (
        'customer', 'product', 'data_hour', 'payment_status',
    )
