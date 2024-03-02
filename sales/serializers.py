from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer')

    class Meta:
        fields = ('id', 'product', 'price', 'quantity', 'customer_name')
        model = Sale
