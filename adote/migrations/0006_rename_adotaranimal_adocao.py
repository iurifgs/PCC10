# Generated by Django 4.2.6 on 2024-08-22 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0012_alter_animal_data_nascimento'),
        ('adote', '0005_adotaranimal_animal'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdotarAnimal',
            new_name='Adocao',
        ),
    ]