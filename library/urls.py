from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='livro_list'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('livro/<int:pk>/editar/', views.editar_livro, name='editar_livro'),
    path('livro/<int:pk>/excluir/', views.excluir_livro, name='excluir_livro'),
    path('', views.listar_livros, name='livro_list'),
    path('livro/novo/', views.adicionar_livro, name='adicionar_livro'),
]

