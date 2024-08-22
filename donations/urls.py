from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.donation_create, name='donation_create'),
    path('update/<int:pk>/', views.donation_update, name='donation_update'),
    path('delete/<int:pk>/', views.donation_delete, name='donation_delete'),
]