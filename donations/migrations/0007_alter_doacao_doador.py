# Generated by Django 4.2.6 on 2024-08-22 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('donations', '0006_alter_doacao_doador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='doador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
    ]
