from sales.models import Sale
from rest_framework import serializers


class SaleSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = '__all__'

    def get_product_name(self, obj):
        return obj.get_product_display()

    def get_customer_name(self, obj):
        return obj.customer.name
