from django.db import models
from usuario.models import Usuario

class Doacao(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    quantia = models.DecimalField(max_digits=10, decimal_places=2)
    mensagem = models.TextField(blank=True, null=True)
    
    #vem da relação - vide diagrama
    doador = models.ForeignKey(Usuario, on_delete=models.CASCADE)    

    def __str__(self):
        return f"Doação de {self.quantia} por {self.doador}"