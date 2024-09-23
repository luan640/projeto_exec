# Generated by Django 4.2.15 on 2024-08-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_funcionario_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='tipo_acesso',
            field=models.CharField(choices=[('solicitante', 'Solicitante'), ('administrador', 'Administrador'), ('operador', 'Operador')], default='solicitante', max_length=50),
        ),
    ]