from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'cidade', 'mensagem', 'assunto']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 4}),
            'assunto': forms.Select()
        }
