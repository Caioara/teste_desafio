
# Desafio referente a Fábrica de Software (Back-End) - UNIPÊ 2024.2 
### OBJETIVO DO DESAFIO :anger: (OPÇÃO 1):
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

# Métodos POST, GET (ou PATCH), DELETE através do INSOMNIA
Uma vez configurada no .Paises/api/viewsets.py, a função “create()” tem esse papel sob a API em si. 
<br>
__OBS:__ Utilizando integralmente ```import requests```.

É definido um valor padrão a variável país, levando em consideração ao input do usuário, no momento do POST.
```
pais = request.data.get('name', '')
```


Defini uma variável "url" usando o nome do {país} como endpoint em cima da API de informações de países. Em sequência, a variável “requisicao”, faz a requisição GET com base na URL, sendo a API. Juntamente ao “json-data” que apenas converte essa resposta a um objeto JSON. 
```
url = f"https://restcountries.com/v2/name/{pais}"
requisicao = requests.get(url)
json_data = requisicao.json()
```

__OBS:__ Ao executar o código não consegui ter um retorno direto da API, foi quando notei que toda estrutura JSON estava dentro de uma lista. Contornei essa situação com o auxílio do Chat GPT :zipper_mouth_face:, que me deu a seguinte solução:
```
if isinstance(json_data, list) and json_data: #Verifica se os dados retornados são uma lista e se ela não está vazia.
            country_info = json_data[0] #Se a condição anterior for verdadeira, assume-se que a primeira entrada na lista contém as informações do país. Essas informações são extraídas para a variável country_info.  
            name = country_info.get('name','')
            capital = country_info.get('capital','')
            subregion = country_info.get('subregion','')
            population = country_info.get('population','')
            region = country_info.get('region','')
```

Por sequência, inicia-se um dicionário onde vai armazenar todas as informações necessárias para o armazenamento no Banco de Dados.
```
        dadosrecebidos = {             
            "name": f'{name}',
            "capital": f'{capital}',
            "subregion": f'{subregion}',
            "population": f'{population}',
            "region": f'{region}',
        }
```

Por fim um algoritmo que exerce a função na administração dos requests, levando em consideração o estado atual do banco de dados, se tem devido elemento, ou se está repetido.
```
meuserializer = PaisSerializer(data=dadosrecebidos)

        if meuserializer.is_valid():
            name_pesquisado = Pais.objects.filter(name=name)
            name_pesquisado_existe = name_pesquisado.exists()

            if name_pesquisado_existe:
                return Response({"AVISO":"Seu País já existe no bando de dados"})
            
            meuserializer.save()
            return Response(meuserializer.data)
            
        else:
            return Response({"AVISO: Algo deu errado"})
```


 #### Agradecimentos especiais(euacho):
- João Pedro: Deixa de dormir para ajudar o próximo :zzz:
- Natan: Enxergou que ninguém nunca ia enxergar :eye_speech_bubble:
- Lucas: Uma didatica foda, sabe oque ta fazendo :nerd_face:
- Raphinha: cep :wrestling:













