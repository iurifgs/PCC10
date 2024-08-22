from django.urls import path
from . import views

urlpatterns = [
    path('adotar_animal/<int:pk>/', views.adotar_animal, name='adotar_animal'),
    path('adotar/<int:id>/', views.adotar, name='adotar'),
    path('listar_adocoes/', views.listar_adocoes, name='listar_adocoes'),
    path('deletar_adocao/<int:pk>/', views.deletar_adocao, name='deletar_adocao'),
    path('editar_adocao/<int:pk>/', views.editar_adocao, name='editar_adocao'),
]