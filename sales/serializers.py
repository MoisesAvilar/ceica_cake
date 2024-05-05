from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('product', 'price', 'quantity', 'data_hour', 'total_sale')
