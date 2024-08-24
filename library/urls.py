from django.urls import path
from . import views

urlpatterns = [
    path('', views.livro_list, name='livro_list'),
    path('livro/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livro/new/', views.livro_create, name='livro_create'),
    path('livro/<int:pk>/edit/', views.livro_update, name='livro_update'),
    path('livro/<int:pk>/delete/', views.livro_delete, name='livro_delete'),
]
