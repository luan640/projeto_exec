# Generated by Django 4.2.15 on 2024-11-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execucao', '0013_rename_quantidade_execucao_paplus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosolicitacao',
            name='tipo_manutencao',
            field=models.CharField(choices=[('corretiva', 'Corretiva'), ('preditiva', 'Preditiva'), ('preventiva_programada', ' Preventiva programada'), ('apoio', 'Apoio'), ('projetos', 'Projetos'), ('sesmt', 'SESMT'), ('corretiva_programada', 'Corretiva programada')], max_length=40),
        ),
    ]
