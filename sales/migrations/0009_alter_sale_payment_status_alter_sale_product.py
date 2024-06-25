# Generated by Django 5.0.2 on 2024-06-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_remove_sale_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='payment_status',
            field=models.CharField(choices=[('PENDENTE', 'Pendente'), ('PAGO', 'Pago')], default='PENDENTE', max_length=20),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.CharField(choices=[('BOLO_DE_POTE_P', 'Bolo de pote P'), ('BOLO_DE_POTE_G', 'Bolo de pote G'), ('BRASINHA_COMUM', 'Brasinha comum'), ('BRASINHA_GOURMET', 'Brasinha gourmet'), ('BOLO_DE_ANIVERSARIO', 'Bolo de aniversário'), ('BOLO_VULCAO_P', 'Bolo vulcão P'), ('BOLO_VULCAO_M', 'Bolo vulcão M'), ('BOLO_VULCAO_G', 'Bolo vulcão G'), ('TORTA', 'Torta')], max_length=30),
        ),
    ]
