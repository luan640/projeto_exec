# Generated by Django 5.0.1 on 2024-08-11 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("execucao", "0006_alter_maquinaparada_data_fim"),
    ]

    operations = [
        migrations.AddField(
            model_name="maquinaparada",
            name="execucao",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="maquina_parada",
                to="execucao.execucao",
            ),
        ),
    ]