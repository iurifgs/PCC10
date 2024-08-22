from django.db import models
from usuario.models import Usuario

class Comentario(models.Model):
    ASSUNTO_CHOICES = [
        ('', 'Selecione'),
        ('Adoção', 'Adoção'),
        ('Sugestões', 'Sugestões'),
        ('Elogios', 'Elogios'),
        ('Reclamações', 'Reclamações'),
        ('Outros', 'Outros'),
    ]

    assunto = models.CharField(max_length=20, choices=ASSUNTO_CHOICES, null=False, blank=False, default='')
    nome = models.CharField(max_length=50, null=False, blank=False, default="Digite seu nome")
    data = models.DateTimeField(auto_now_add=True)
    cidade = models.CharField(max_length=50, default="Informe sua cidade")
    mensagem = models.CharField(max_length=500, null=False, blank=False, default='')


    user = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.mensagem[:50]