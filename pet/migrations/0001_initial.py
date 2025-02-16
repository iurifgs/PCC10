# Generated by Django 4.2.6 on 2024-05-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=50)),
                ('raca', models.CharField(blank=True, default='Desconhecida', max_length=50, null=True)),
                ('data_nascimento', models.DateField(default='2024-05-27')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
            ],
        ),
    ]
