# Generated by Django 4.2.6 on 2024-08-22 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('denuncia', '0003_alter_denuncia_denunciante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='denunciante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
    ]
