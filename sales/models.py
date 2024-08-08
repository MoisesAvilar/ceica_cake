from django.db import models
from customers.models import Customer


PRODUCT = (
    ('TORTA', 'Torta'),
    ('BROWNIE', 'Brownie'),
    ('BRASINHA_COMUM', 'Brasinha comum'),
    ('BRASINHA_GOURMET', 'Brasinha gourmet'),
    ('BOLO_DE_POTE_P', 'Bolo de pote P'),
    ('BOLO_DE_POTE_G', 'Bolo de pote G'),
    ('BOLO_VULCAO_P', 'Bolo vulcão P'),
    ('BOLO_VULCAO_M', 'Bolo vulcão M'),
    ('BOLO_VULCAO_G', 'Bolo vulcão G'),
    ('BOLO_DE_ANIVERSARIO', 'Bolo de aniversário'),
)

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

    def save(self, *args, **kwargs):
        if self.pk:
            existing_sale = Sale.objects.get(pk=self.pk)
            self.customer.bought -= existing_sale.total

            if existing_sale.payment_status == 'PENDENTE' and self.payment_status == 'PAGO':
                self.customer.bought -= self.total
            elif existing_sale.payment_status == 'PAGO' and self.payment_status == 'PENDENTE':
                self.customer.bought += self.total

        self.total = self.price * self.quantity
        super().save(*args, **kwargs)

        self.customer.bought += self.total
        self.customer.save()

    def __str__(self):
        return self.product
