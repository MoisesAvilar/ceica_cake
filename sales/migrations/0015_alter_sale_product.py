from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_alter_sale_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.CharField(choices=[
                ('TORTA', 'Torta'),
                ('TORTA_DE_PAO', 'Torta de pão'),
                ('TORTA_NO_POTE', 'Torta no pote'),
                ('BRASINHA_COMUM', 'Brasinha comum'),
                ('BRASINHA_GOURMET', 'Brasinha gourmet'),
                ('TRUFA', 'Trufa'),
                ('BROWNIE', 'Brownie'),
                ('BRIGADEIRO', 'Brigadeiro'),
                ('FATIA_COM_DOCE', 'Fatia com doce'),
                ('FATIA_SEM_DOCE', 'Fatia sem doce'),
                ('BOLO_DE_POTE_P', 'Bolo de pote P'),
                ('BOLO_DE_POTE_G', 'Bolo de pote G'),
                ('BOLO_VULCAO_P', 'Bolo vulcão P'),
                ('BOLO_VULCAO_M', 'Bolo vulcão M'),
                ('BOLO_VULCAO_G', 'Bolo vulcão G'),
                ('BOLO_VULCAO_GG', 'Bolo vulcão GG'),
                ('BOLO_DE_ANIVERSARIO', 'Bolo de aniversário'),
                ('MINI_COPO_DA_FELICIDADE', 'Mini copo da felicidade'),
                ('COPO_DA_FELICIDADE', 'Copo da felicidade'),
                ('PANETONE_TRUFADO', 'Panetone trufado'),
            ], max_length=30),
        ),
    ]
