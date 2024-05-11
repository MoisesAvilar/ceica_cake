from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from sales.models import Sale


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(payment_status='PAGO')


mark_as_paid.short_description = 'Marcar como pago'


@admin.register(Sale)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'quantity', 'price', 'customer_link', 'data_hour',
        'payment_status', 'total',
    )

    list_filter = (
        'customer', 'product', 'data_hour', 'payment_status', 'total',
    )

    actions = [mark_as_paid]

    def customer_link(self, obj):
        url = reverse('admin:customers_customer_change', args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', url, obj.customer.name)
    customer_link.short_description = 'Customer'
    customer_link.admin_order_field = 'customer'
