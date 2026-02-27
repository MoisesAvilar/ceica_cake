from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from customers.models import Customer
from sales.product_list import PRODUCT

PAYMENT_STATUS = (
    ("PENDENTE", "Pendente"),
    ("PAGO", "Pago"),
)


class Sale(models.Model):
    product = models.CharField(max_length=30, choices=PRODUCT)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    data_hour = models.DateTimeField(default=timezone.now)
    payment_status = models.CharField(
        default="PENDENTE", max_length=20, choices=PAYMENT_STATUS
    )
    total = models.FloatField(default=0, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity

        if self.pk:
            old_sale = Sale.objects.get(pk=self.pk)
            if old_sale.payment_status == "PAGO":
                self.customer.bought -= old_sale.total
            else:
                self.customer.debt -= old_sale.total

        if self.payment_status == "PAGO":
            self.customer.bought += self.total
        else:
            self.customer.debt += self.total

        self.customer.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_product_display()} - {self.customer.name}"
