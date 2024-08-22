from django.urls import path
from django.shortcuts import render
from . import views
from .views import contato

urlpatterns = [
    path('criar/', views.criar_comentario, name='criar_comentario'),
    path('editar/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('excluir/<int:id>/', views.excluir_comentario, name='excluir_comentario'),
    path('contato/', contato, name='contato'),
    path('obrigado/', lambda request: render(request, 'obrigado.html'), name='obrigado'),
]