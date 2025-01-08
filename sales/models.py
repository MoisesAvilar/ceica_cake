from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from sales.product_list import PRODUCT


PAYMENT_STATUS = (
    ('PENDENTE', 'Pendente'),
    ('PAGO', 'Pago'),
)


class Sale(models.Model):
    product = models.CharField(max_length=30, choices=PRODUCT)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    data_hour = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(default='PENDENTE', max_length=20, choices=PAYMENT_STATUS)
    total = models.FloatField(default=0, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity

        if self.pk:
            existing_sale = Sale.objects.get(pk=self.pk)
            previous_total = existing_sale.total

            if existing_sale.payment_status == 'PAGO':
                self.customer.bought -= previous_total
            elif existing_sale.payment_status == 'PENDENTE':
                self.customer.debt -= previous_total

        if self.payment_status == 'PAGO':
            self.customer.bought += self.total
        elif self.payment_status == 'PENDENTE':
            self.customer.debt += self.total

        super().save(*args, **kwargs)
        self.customer.save()
