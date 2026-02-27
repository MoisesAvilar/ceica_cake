from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sale
from cashflow.models import Cashflow


@receiver(post_save, sender=Sale)
def update_cashflow_on_sale(sender, instance, created, **kwargs):
    if instance.payment_status == 'PAGO':
        unique_ref = f"ID-REF-{instance.id}"
        display_description = f"Venda: {instance.get_product_display()} - Cliente: {instance.customer.name} ({unique_ref})"
        
        Cashflow.objects.update_or_create(
            description__icontains=unique_ref,
            defaults={
                'category': "Venda",
                'value': instance.total,
                'value_type': "PROFIT",
                'date': instance.data_hour.date(),
                'description': display_description
            }
        )
    elif not created and instance.payment_status == 'PENDENTE':
        unique_ref = f"ID-REF-{instance.id}"
        Cashflow.objects.filter(description__icontains=unique_ref).delete()
