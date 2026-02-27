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
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.title()

        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name