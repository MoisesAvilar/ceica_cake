# Generated by Django 5.0.2 on 2024-06-10 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_sale_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product_description',
        ),
    ]