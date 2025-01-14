# Generated by Django 4.2.6 on 2024-08-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_rename_menssagem_donation_mensagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mensagem', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
