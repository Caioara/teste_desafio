import os
import django

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from library.models import Categoria

def add_default_categories():
    categorias = ['Mangá', 'Ficção Científica', 'Fantasia', 'Romance']
    
    for categoria in categorias:
        Categoria.objects.get_or_create(nome=categoria)

if __name__ == "__main__":
    add_default_categories()
    print("Categorias padrão adicionadas.")
