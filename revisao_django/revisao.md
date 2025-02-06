
### **1. Introdução ao Django**  
**Objetivo:** Relembrar a estrutura e propósito do Django.  
- **O que é Django?**  
  - Framework web Python para desenvolvimento rápido, seguro e escalável.  
  - Segue o padrão **MVT** (Model-View-Template), uma variação do MVC.  

- **Principais Características:**  
  - ORM (Mapeamento Objeto-Relacional) para banco de dados.  
  - Sistema de templates poderoso.  
  - Painel de administração automático (`admin`).  
  - Sistema de rotas e middlewares.  

---

### **2. Estrutura de um Projeto Django**  
**Objetivo:** Revisar a organização de diretórios e arquivos.  

- **Comandos Iniciais:**  
  ```bash  
  django-admin startproject nome_projeto  # Cria um novo projeto  
  python manage.py startapp nome_app      # Cria uma nova aplicação  
  ```  

- **Arquivos Principais:**  
  - `settings.py`: Configurações do projeto (BD, apps instaladas, middlewares).  
  - `urls.py`: Define as rotas do projeto.  
  - `models.py`: Define os modelos de dados (BD).  
  - `views.py`: Lógica de negócio (controladores).  
  - `templates/`: Arquivos HTML com sintaxe Django.  

---

### **3. Models e ORM**  
**Objetivo:** Relembrar a criação de modelos e consultas ao banco de dados.  

- **Exemplo de Modelo:**  
  ```python  
  from django.db import models  

  class Produto(models.Model):  
      nome = models.CharField(max_length=100)  
      preco = models.DecimalField(max_digits=10, decimal_places=2)  
      estoque = models.IntegerField()  
      data_criacao = models.DateTimeField(auto_now_add=True)  
  ```  

- **Consultas com ORM:**  
  ```python  
  # SELECT * FROM produto WHERE estoque > 0  
  produtos = Produto.objects.filter(estoque__gt=0)  

  # INSERT  
  novo_produto = Produto(nome="Camiseta", preco=99.90, estoque=10)  
  novo_produto.save()  
  ```  

---

### **4. Views e URLs**  
**Objetivo:** Revisar a conexão entre views, URLs e templates.  

- **View Baseada em Função:**  
  ```python  
  from django.shortcuts import render  
  from .models import Produto  

  def lista_produtos(request):  
      produtos = Produto.objects.all()  
      return render(request, 'produtos/lista.html', {'produtos': produtos})  
  ```  

- **Configurando a URL:**  
  ```python  
  # urls.py  
  from django.urls import path  
  from . import views  

  urlpatterns = [  
      path('produtos/', views.lista_produtos, name='lista_produtos'),  
  ]  
  ```  

---

### **5. Templates e Template Tags**  
**Objetivo:** Relembrar a sintaxe de templates e herança.  

- **Exemplo de Template:**  
  ```html  
  <!-- lista.html -->  
  {% extends 'base.html' %}  

  {% block content %}  
  <h1>Produtos</h1>  
  <ul>  
      {% for produto in produtos %}  
          <li>{{ produto.nome }} - R$ {{ produto.preco }}</li>  
      {% endfor %}  
  </ul>  
  {% endblock %}  
  ```  

- **Principais Template Tags:**  
  - `{% if %}`, `{% for %}`: Estruturas condicionais e loops.  
  - `{% url 'nome_rota' %}`: Gera URLs dinâmicas.  
  - `{% include 'arquivo.html' %}`: Inclui templates parcialmente.  

---

### **6. Formulários e Validação**  
**Objetivo:** Revisar a criação e validação de formulários.  

- **Formulário Baseado em Modelo:**  
  ```python  
  from django import forms  
  from .models import Produto  

  class ProdutoForm(forms.ModelForm):  
      class Meta:  
          model = Produto  
          fields = ['nome', 'preco', 'estoque']  
  ```  

- **Processamento na View:**  
  ```python  
  def criar_produto(request):  
      if request.method == 'POST':  
          form = ProdutoForm(request.POST)  
          if form.is_valid():  
              form.save()  
              return redirect('lista_produtos')  
      else:  
          form = ProdutoForm()  
      return render(request, 'produtos/form.html', {'form': form})  
  ```  

---

### **7. Painel de Administração (Admin)**  
**Objetivo:** Personalizar o painel admin.  

- **Registrando um Modelo:**  
  ```python  
  from django.contrib import admin  
  from .models import Produto  

  @admin.register(Produto)  
  class ProdutoAdmin(admin.ModelAdmin):  
      list_display = ['nome', 'preco', 'estoque']  
      search_fields = ['nome']  
  ```  

---

### **8. Middleware e Context Processors**  
**Objetivo:** Relembrar conceitos avançados.  
- **Middleware:** Camadas que processam requests/responses (ex: autenticação).  
- **Context Processors:** Adicionam variáveis globais aos templates (ex: `request.user`).  

---

### **9. Segurança no Django**  
**Objetivo:** Revisar práticas de segurança.  
- **Proteções Automáticas:**  
  - CSRF (Cross-Site Request Forgery): Token em formulários.  
  - XSS (Cross-Site Scripting): Escape automático em templates.  
  - SQL Injection: Prevenido pelo ORM.  

---

### **10. Deploy e Boas Práticas**  
- **Serviços Populares:** Heroku, AWS, DigitalOcean, Render.  
- **Checklist para Deploy:**  
  - Configurar `DEBUG = False`.  
  - Definir `ALLOWED_HOSTS`.  
  - Coletar arquivos estáticos (`python manage.py collectstatic`).  

---

### **Exercício Prático (Para Fixação):**  
1. Crie uma aplicação de blog com:  
   - Modelo `Post` (título, conteúdo, data_publicacao).  
   - View para listar posts recentes.  
   - Formulário para criar novos posts (apenas para usuários autenticados).  
   - Template com herança e exibição condicional.  

---

**Recursos Adicionais:**  
- [Documentação Oficial do Django](https://docs.djangoproject.com/)  
- Livro: "Django for Beginners" (William S. Vincent)  

**Próximos Passos:**  
- Aprofundar em REST APIs com Django REST Framework.  
- Explorar autenticação com `django-allauth`.  