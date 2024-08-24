
# Desafio referente a Fábrica de Software (Back-End) - UNIPÊ 2024.2 
### OBJETIVO DO DESAFIO :anger: :
  Criar um Projeto Django em Template ou API
#### REQUISITOS FUNCIONAIS
  
  - [x] Deve possuir todo o CRUD do django com duas ou mais entidades
  - [x] Deve sem bem documentado, contendo Requirenents.txt e README.md.
  - [x] Possua a capacidade de consumir uma API externa gratuita(Sem token de autenticação) da escolha do usuário para guardar um dado.
            
#### REQUISITOS NÃO FUNCIONAIS

  - [x] Indentação do Código.
  - [x] Estruturação do Código (Pastas, Classes e Arquivos con nomes concisos e referentes).

#### PONTUAÇÃO EXTRA
- [x] página funcional e organizada com HTML e CSS (Django template).
- [x] Commits Semânticos

## Requerimentos
1. asgiref
2. certifi
3. charset-normalizer
4. Django
5. djangorestframework
6. requests
7. mais sobre no próprios arquivo requirements.txt...

# Para rodar :dizzy:
É necessário fazer algumas ações. Certifique-se de ter o Python e instalados. Em seguida, crie um novo ambiente virtual ```py -m venv {nome_da_venv}```, e __entre nela__ ```.\{nome_da_venv}\Scripts\activate```.
<br><br>
Em seguinda instale as __dependências:__
```
pip install django
pip install django djangorestframework
pip install requests
```





# Escolha da API
A princípio, minha prioridade era escolher uma API simples, que me retornasse dados de maneira limpa e que de certa forma fossem fáceis de manipular. A API em questão foi a [Open Library Books API]([https://restcountries.com/](https://rapidapi.com/blog/directory/open-library-books/)), que fornece dados sobre livros com base em ISBNs e outros identificadores, oferecendo informações como título, autor e detalhes de publicação.
# Acesso a API

Antes de qualquer coisa é necessario dentro do seu aplicativo Django:
Configurar o seu Arquivo views.py dessa maneira:
```
import requests
from django.shortcuts import render, redirect
from django.contrib import messages

def buscar_livro_por_isbn(isbn):
    url = f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data'
    response = requests.get(url)
    return response.json()

def adicionar_livro(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        data = buscar_livro_por_isbn(isbn)
        book_key = f'ISBN:{isbn}'
        if book_key in data:
            book = data[book_key]
            # Processar os dados do livro e salvar no banco de dados
            # Exemplo: Livro.objects.create(titulo=book['title'], ...)
            messages.success(request, f"Livro {book['title']} adicionado com sucesso!")
            return redirect('livro_list')
        else:
            messages.error(request, "Livro não encontrado na API.")
    return render(request, 'adicionar_livro.html')
 ```
E depois na urls.py tambem configurar desse jeito:
```
from django.urls import path
from .views import adicionar_livro

urlpatterns = [
    path('adicionar/', adicionar_livro, name='adicionar_livro'),
]
 
```
E finalizando criando dentro da template de do aplicativo se não tiver um "adicionar_livro.html" e configurando desse jeito:
```
<!DOCTYPE html>
<html>
<head>
    <title>Adicionar Livro</title>
</head>
<body>
    <h1>Adicionar Novo Livro</h1>
    <form method="post">
        {% csrf_token %}
        <label for="isbn">ISBN:</label>
        <input type="text" id="isbn" name="isbn" required>
        <button type="submit">Adicionar Livro</button>
    </form>
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>

```

 #### Agradecimentos:
- Nattan: Dando aquele supporte maroto :nerd_face:
- Lucas: Uma didatica foda, sabe oque ta fazendo :nerd_face:














