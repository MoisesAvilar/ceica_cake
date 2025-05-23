# Generated by Django 5.0.2 on 2025-01-11 03:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cashflow',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
