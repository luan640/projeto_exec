# Generated by Django 4.2.15 on 2024-08-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0002_alter_solicitacao_equipamento_em_falha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='codigo_ferramenta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='tipo_ferramenta',
            field=models.CharField(choices=[('esmerilhadeira', 'Esmerilhadeira'), ('tocha', 'Tocha')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
