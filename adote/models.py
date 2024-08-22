from django.db import models
from django.utils import timezone
from pet.models import Animal


class Adocao(models.Model):

    data_adocao = models.DateField(default=timezone.now)

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Adotação de Animal'
        verbose_name_plural = 'Adoções de Animais'

    def __str__(self):
        return f"{self.animal.nome}"