from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Livro
from .forms import CategoriaForm, LivroForm
import requests

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livro_list.html', {'livros': livros})

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livro_detail.html', {'livro': livro})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            # Consome a API externa
            response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{livro.isbn}&format=json")
            data = response.json()
            if f"ISBN:{livro.isbn}" in data:
                info = data[f"ISBN:{livro.isbn}"]
                livro.titulo = info.get('title', livro.titulo)
                livro.autor = ", ".join(author['name'] for author in info.get('authors', []))
                livro.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_list')
    return render(request, 'livro_confirm_delete.html', {'livro': livro})


# Create your views here.
