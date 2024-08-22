from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'telefone', 'cep', 'cidade', 'estado', 'estado_civil_adotante')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'telefone', 'cep', 'cidade', 'estado', 'estado_civil_adotante')