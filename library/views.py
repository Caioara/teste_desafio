import requests
from django.shortcuts import render, redirect
from .models import Livro, Categoria
from .forms import LivroForm

# Função de busca na API
def buscar_livro_por_isbn(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if f"ISBN:{isbn}" in data:
            return data[f"ISBN:{isbn}"]
    return None

# View para adicionar um novo livro
def adicionar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            livro_info = buscar_livro_por_isbn(isbn)
            if livro_info:
                livro = form.save(commit=False)
                livro.titulo = livro_info.get('title', livro.titulo)
                livro.autor = ", ".join([author['name'] for author in livro_info.get('authors', [])])
                livro.save()
                return redirect('livro_list')
            else:
                form.add_error('isbn', f'Livro com ISBN {isbn} não encontrado na API.')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form': form})

# View para listar os livros
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livro_list.html', {'livros': livros})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm

# View para editar um livro
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form': form, 'editar': True})

# View para excluir um livro
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect('livro_list')
    return render(request, 'confirmar_exclusao.html', {'livro': livro})


# Create your views here.
