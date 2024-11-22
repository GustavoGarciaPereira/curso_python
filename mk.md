Aqui estão exemplos práticos para cada etapa mencionada no aprendizado de Django com Python:

---

### **1. Fundamentos de Python**
- **Exemplo de função:**
  ```python
  def soma(a, b):
      return a + b

  resultado = soma(5, 7)
  print(f"A soma é: {resultado}")
  ```

- **Exemplo de manipulação de listas:**
  ```python
  frutas = ["maçã", "banana", "laranja"]
  for fruta in frutas:
      print(fruta.upper())
  ```

- **Exemplo de Orientação a Objetos:**
  ```python
  class Pessoa:
      def __init__(self, nome, idade):
          self.nome = nome
          self.idade = idade

      def apresentar(self):
          print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

  pessoa = Pessoa("Gustavo", 25)
  pessoa.apresentar()
  ```

---

### **2. Ambiente de Desenvolvimento**
- **Criar e ativar um ambiente virtual:**
  ```bash
  python -m venv meu_ambiente
  source meu_ambiente/bin/activate  # Linux/Mac
  meu_ambiente\Scripts\activate     # Windows
  ```

---

### **3. Django: Introdução**
- **Criar um projeto Django:**
  ```bash
  django-admin startproject meu_projeto
  cd meu_projeto
  python manage.py runserver
  ```
  Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

- **Criar um app chamado `blog`:**
  ```bash
  python manage.py startapp blog
  ```

---

### **4. Estrutura do Django**
- **Adicionar uma URL e view simples:**

  **`meu_projeto/urls.py`**
  ```python
  from django.contrib import admin
  from django.urls import path
  from blog import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.index),  # Adiciona a URL do app blog
  ]
  ```

  **`blog/views.py`**
  ```python
  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Bem-vindo ao meu blog!")
  ```

---

### **5. Django em Profundidade**
- **Adicionar um modelo simples:**

  **`blog/models.py`**
  ```python
  from django.db import models

  class Post(models.Model):
      titulo = models.CharField(max_length=100)
      conteudo = models.TextField()
      data_publicacao = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.titulo
  ```

- **Criar a tabela no banco de dados:**
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Adicionar um post via Django Admin:**
  ```bash
  python manage.py createsuperuser
  python manage.py runserver
  ```
  Acesse: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

### **6. Práticas Avançadas**
- **Formulário para criar posts:**

  **`blog/forms.py`**
  ```python
  from django import forms
  from .models import Post

  class PostForm(forms.ModelForm):
      class Meta:
          model = Post
          fields = ['titulo', 'conteudo']
  ```

  **`blog/views.py`**
  ```python
  from django.shortcuts import render, redirect
  from .forms import PostForm

  def criar_post(request):
      if request.method == 'POST':
          form = PostForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('/')
      else:
          form = PostForm()
      return render(request, 'criar_post.html', {'form': form})
  ```

  **`blog/templates/criar_post.html`**
  ```html
  <h1>Criar novo post</h1>
  <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Salvar</button>
  </form>
  ```

---

### **7. Deploy**
- **Deploy básico com Heroku:**
  1. **Instalar Heroku CLI** e dependências:
     ```bash
     pip install gunicorn django-heroku
     ```
  2. **Adicionar ao `settings.py`:**
     ```python
     import django_heroku
     django_heroku.settings(locals())
     ```

  3. **Criar um arquivo `Procfile`:**
     ```bash
     echo "web: gunicorn meu_projeto.wsgi" > Procfile
     ```

  4. **Subir para o Heroku:**
     ```bash
     git init
     heroku create
     git push heroku main
     ```

---

### **Exemplo de Projeto Prático**
- **Blog com CRUD (Create, Read, Update, Delete):**
  1. Crie um modelo `Post` no banco.
  2. Adicione views para listar, criar, editar e excluir posts.
  3. Construa templates HTML para cada ação.

- **E-commerce simples:**
  - Modelos para produtos, carrinho de compras e pedidos.
  - Sistema de autenticação para usuários.

Esses exemplos práticos te ajudam a aplicar o conhecimento conforme você avança no aprendizado!