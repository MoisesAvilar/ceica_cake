from django.db import models
from django.core.validators import MinLengthValidator


class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11, "Digite no padrão (**) *****-****"),
        ],
    )
    birthday = models.DateField(blank=True, null=True)
    bought = models.FloatField(default=0.0)
    debt = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
