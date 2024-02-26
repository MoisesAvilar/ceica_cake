from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Sale
