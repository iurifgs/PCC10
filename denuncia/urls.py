from django.urls import path
from . import views

urlpatterns = [
    path('denuncias/', views.denuncia_list, name='denuncia_list'),
    path('denuncias/nova/', views.denuncia_create, name='denuncia_create'),
    path('denuncias/<int:pk>/editar/', views.denuncia_update, name='denuncia_update'),
    path('denuncias/<int:pk>/apagar/', views.denuncia_delete, name='denuncia_delete'),
]