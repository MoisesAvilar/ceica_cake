from django.db import models
from customers.models import Customer


PRODUCT = (
    ('BOLO_DE_POTE_P', 'Bolo de pote P'),
    ('BOLO_DE_POTE_G', 'Bolo de pote G'),
    ('BRASINHA_COMUM', 'Brasinha comum'),
    ('BRASINHA_GOURMET', 'Brasinha gourmet'),
    ('BOLO_DE_ANIVERSARIO', 'Bolo de aniversário'),
    ('BOLO_VULCAO', 'Bolo vulcão'),
    ('TORTA', 'Torta')
)

PAYMENT_STATUS = (
    ('PENDENTE', 'Pendente'),
    ('PAGO', 'Pago'),
)


class Sale(models.Model):
    product = models.CharField(max_length=30, choices=PRODUCT)
    product_description = models.CharField(max_length=50, default='')
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    data_hour = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(default='Pendente', max_length=20, choices=PAYMENT_STATUS)
    total = models.FloatField(default=0, editable=False)

    def save(self, *args, **kwargs):
        if self.pk:
            existing_sale = Sale.objects.get(pk=self.pk)
            self.customer.bought -= existing_sale.total

        for product_code, description in PRODUCT:
            if product_code == self.product:
                self.product_description = description
                break

        self.total = self.price * self.quantity
        super().save(*args, **kwargs)

        self.customer.bought += self.total
        self.customer.save()

    def __str__(self):
        return self.product
