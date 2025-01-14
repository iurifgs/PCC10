# Generated by Django 4.2.6 on 2024-07-30 05:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdotarAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_adotante', models.CharField(default='Não Informado', max_length=100)),
                ('estado_civil_adotante', models.CharField(default='Não Informado', max_length=50)),
                ('data_adocao', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Adotação de Animal',
                'verbose_name_plural': 'Adoções de Animais',
            },
        ),
    ]
