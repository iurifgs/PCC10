# Generated by Django 4.2.6 on 2024-08-05 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comentario_assunto_comentario_cidade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='texto',
        ),
    ]
