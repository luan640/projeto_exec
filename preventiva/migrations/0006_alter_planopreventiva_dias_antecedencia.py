# Generated by Django 4.2.15 on 2024-10-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventiva', '0005_planopreventiva_dias_antecedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planopreventiva',
            name='dias_antecedencia',
            field=models.IntegerField(blank=True, help_text='Com quantos dias antes deverá abrir?', null=True),
        ),
    ]
