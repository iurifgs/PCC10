from django.db import models
from django.contrib.auth.models import User

class Usuario(User):

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
    ]


    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=8) 
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2) 
    estado_civil_adotante = models.CharField(
    max_length=50,
    choices=ESTADO_CIVIL_CHOICES,
    null=False,
    blank=False,
    default='solteiro' 
)

    def __str__(self):
        return self.username