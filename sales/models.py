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


class Sale(models.Model):
    product = models.CharField(max_length=30, choices=PRODUCT)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    @property
    def total_sale(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.customer.bought += self.total_sale
        self.customer.save()

    def __str__(self):
        return self.product
