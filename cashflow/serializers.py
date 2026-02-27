from rest_framework import serializers
from cashflow.models import Cashflow


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = "__all__"

    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser maior que zero.")
        return value
