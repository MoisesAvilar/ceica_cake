from django.contrib import admin
from sales.models import Sale


@admin.register(Sale)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'total_sale', 'customer')
    list_filter = ('product',)
