from django.db import models
from usuario.models import Usuario


class Denuncia(models.Model):
    denunciante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    animal = models.CharField(max_length=100)
    motivo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.animal