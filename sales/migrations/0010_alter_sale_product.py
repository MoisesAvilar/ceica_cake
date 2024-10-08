# Generated by Django 5.0.2 on 2024-08-08 02:09

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_alter_sale_payment_status_alter_sale_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.CharField(
                choices=[
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
                ],
                max_length=30,
            ),
        ),
    ]
