from django import forms
from .models import Adocao
from django.core.exceptions import ValidationError
from django.utils import timezone

class AdotarAnimalForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['data_adocao']
        widgets = {
            'data_adocao': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        


        data_adocao = cleaned_data.get("data_adocao")

    
        if data_adocao and data_adocao > timezone.now().date():
            self.add_error('data_adocao', "A data de adoção não pode ser no futuro.")

        return cleaned_data
