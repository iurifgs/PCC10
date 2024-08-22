from django import forms
from .models import Doacao

class DonationForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['quantia', 'mensagem']

    def clean_quantia(self):
        quantia = self.cleaned_data.get('quantia')
        if quantia <= 0:
            raise forms.ValidationError("O valor da doação deve ser positivo.")
        return quantia