from rest_framework import serializers
from cashflow.models import Cashflow


class CashflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashflow
        fields = '__all__'
