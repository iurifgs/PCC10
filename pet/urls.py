from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.readall, name='index'),
    path('create/', views.create, name='Criar'),
    path('read/<int:id_animal>/', views.read, name='Ler'),
    path('update/<int:id_animal>/', views.update, name='Atualizar'),
    path('delete/<int:id_animal>/', views.delete, name='Deletar'),
    path('delete/confirm/<int:id_animal>/', views.confirmdelete, name='pet_confirm_delete'),
    path('user_index/', views.user_index, name='user_index'),
    path('user_detail/<int:animal_id>/', views.user_detail, name='user_detail'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('apadrinhar/<int:animal_id>/', views.apadrinhar_view, name='apadrinhar_animal'),
    path('apadrinhamento/<int:animal_id>/', views.apadrinhamento_detalhes, name='apadrinhamento_detalhes'),
    path('about/', views.about, name='about'),
    path('vet/', views.veterinarian, name='veterinarian'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('comentarios/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('admin/', views.admin, name='admin'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]