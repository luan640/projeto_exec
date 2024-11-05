# Generated by Django 4.2.15 on 2024-10-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0015_alter_maquina_tombamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='PecaUtilizada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('valor', models.FloatField(default=0)),
            ],
        ),
    ]
