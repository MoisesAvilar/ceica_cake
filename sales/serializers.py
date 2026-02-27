from rest_framework import serializers
from django.db import transaction
from django.utils import timezone
from sales.models import Sale, PAYMENT_STATUS
from customers.models import Customer
from sales.product_list import PRODUCT


class SaleSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ("user",)

    def get_product_name(self, obj):
        return obj.get_product_display()

    def get_customer_name(self, obj):
        return obj.customer.name

    def get_user_name(self, obj):
        if obj.user:
            return obj.user.username
        return None


class CartItemSerializer(serializers.Serializer):
    product = serializers.ChoiceField(choices=PRODUCT)
    quantity = serializers.IntegerField(default=1)
    price = serializers.FloatField()


class CheckoutSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    payment_status = serializers.ChoiceField(choices=PAYMENT_STATUS, default="PENDENTE")
    items = CartItemSerializer(many=True)

    def create(self, validated_data):
        customer = validated_data["customer"]
        payment_status = validated_data["payment_status"]
        items_data = validated_data["items"]
        user = self.context["request"].user

        now = timezone.now()
        sales = []
        with transaction.atomic():
            for item in items_data:
                sale = Sale.objects.create(
                    customer=customer,
                    payment_status=payment_status,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["price"],
                    user=user,
                    data_hour=now,
                )
                sales.append(sale)
        return sales
