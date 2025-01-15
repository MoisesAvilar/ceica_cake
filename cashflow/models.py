from django.db import models
from django.core.exceptions import ValidationError


VALUE_TYPE = (
    ('EXPENSE', 'Gasto'),
    ('PROFIT', 'Lucro'),
)


class Cashflow(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(max_length=50)
    date = models.DateField()
    value_type = models.CharField(max_length=8, choices=VALUE_TYPE)
    description = models.TextField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def clean(self):
        if self.value <= 0:
            raise ValidationError("Value field must be greater than zero.")

    def __str__(self):
        return f'{self.get_value_type_display()}: {self.category} R${self.value:.2f}'
