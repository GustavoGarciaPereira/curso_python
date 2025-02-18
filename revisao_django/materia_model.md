## **1. Extendendo o Model `Pessoa`**
Adicione campos úteis e relacione com outros modelos:

```python
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_aniversario = models.DateField()
    url_portfolio = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='pessoas/', blank=True, null=True)
    
    # Campos calculados/automáticos (não precisam ser preenchidos)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    # Relacionamentos
    habilidades = models.ManyToManyField('Habilidade', blank=True)

    @property
    def idade(self):
        return (now().date() - self.data_aniversario).days // 365

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    def get_absolute_url(self):
        return reverse('detalhe_pessoa', args=[str(self.id)])

# Modelo adicional para habilidades
class Habilidade(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
```

---

## **2. Views (CRUD + Extras)**
Crie views para operações básicas e customizadas:

```python
# views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pessoa, Habilidade

class PessoaListView(ListView):
    model = Pessoa
    template_name = 'pessoas/lista.html'
    context_object_name = 'pessoas'
    paginate_by = 10

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = 'pessoas/detalhe.html'

class PessoaCreateView(CreateView):
    model = Pessoa
    template_name = 'pessoas/form.html'
    fields = ['nome', 'sobrenome', 'data_aniversario', 'url_portfolio', 'imagem', 'habilidades']
    success_url = '/pessoas/'

class PessoaUpdateView(UpdateView):
    model = Pessoa
    template_name = 'pessoas/form.html'
    fields = ['nome', 'sobrenome', 'data_aniversario', 'url_portfolio', 'imagem', 'habilidades']

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'pessoas/confirmar_exclusao.html'
    success_url = '/pessoas/'

# View para buscar pessoas
def buscar_pessoa(request):
    if request.method == 'GET':
        termo = request.GET.get('q')
        pessoas = Pessoa.objects.filter(nome__icontains=termo)
        return render(request, 'pessoas/lista.html', {'pessoas': pessoas})
```

---

## **3. Templates (Exemplos)**
Estrutura básica de templates:

### **base.html (Template Base)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Portfólios</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### **lista.html (Lista de Pessoas)**
```html
{% extends 'base.html' %}

{% block content %}
<h1>Pessoas</h1>
<a href="{% url 'criar_pessoa' %}" class="btn btn-primary mb-3">Nova Pessoa</a>

<form method="get" action="{% url 'buscar_pessoa' %}">
    <input type="text" name="q" placeholder="Buscar...">
    <button type="submit" class="btn btn-secondary">Buscar</button>
</form>

<div class="row">
    {% for pessoa in pessoas %}
    <div class="col-md-4 mb-4">
        <div class="card">
            {% if pessoa.imagem %}
            <img src="{{ pessoa.imagem.url }}" class="card-img-top" alt="{{ pessoa.nome }}">
            {% endif %}
            <div class="card-body">
                <h5 class="card-title">{{ pessoa.nome }} {{ pessoa.sobrenome }}</h5>
                <p class="card-text">Idade: {{ pessoa.idade }}</p>
                <a href="{{ pessoa.get_absolute_url }}" class="btn btn-info">Ver Detalhes</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

### **detalhe.html (Detalhes da Pessoa)**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>{{ pessoa.nome }} {{ pessoa.sobrenome }}</h1>
    <p>Idade: {{ pessoa.idade }}</p>
    <p>Portfólio: <a href="{{ pessoa.url_portifolio }}" target="_blank">{{ pessoa.url_portifolio }}</a></p>
    <p>Habilidades: {% for habilidade in pessoa.habilidades.all %}{{ habilidade }}{% if not forloop.last %}, {% endif %}{% endfor %}</p>
    
    {% if pessoa.imagem  %}
        <img src="{{ pessoa.imagem.url }}" class="img-fluid" alt="{{ pessoa.nome }}">
    {% endif %}
    <a href="{% url 'editar_pessoa' pessoa.id %}" class="btn btn-warning">Editar</a>
    <a href="{% url 'excluir_pessoa' pessoa.id %}" class="btn btn-danger">Excluir</a>
    <a href="{% url 'lista_pessoas' %}" class="btn btn-secondary">Voltar</a>
{% endblock %}
```
### **versão 1**
```html
{% extends 'base.html' %}

{% block content %}
<h1>{{ titulo }}</h1>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Salvar</button>
</form>
<a href="{% url 'lista_pessoas' %}" class="btn btn-secondary mt-3">Voltar</a>
{% endblock %}
```
### **versão 2**
```html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <h1 class="mb-4">{{ titulo }}</h1>
    <form method="post" enctype="multipart/form-data" class="needs-validation" novalidate>
        {% csrf_token %}
        <div class="mb-3">
            {{ form.nome.label_tag }}
            {{ form.nome }}
            <div class="invalid-feedback">
                Por favor, insira um nome válido.
            </div>
        </div>
        <div class="mb-3">
            {{ form.sobrenome.label_tag }}
            {{ form.sobrenome }}
            <div class="invalid-feedback">
                Por favor, insira um sobrenome válido.
            </div>
        </div>
        <div class="mb-3">
            {{ form.data_aniversario.label_tag }}
            {{ form.data_aniversario }}
            <div class="invalid-feedback">
                Por favor, insira uma data de aniversário válida.
            </div>
        </div>
        <div class="mb-3">
            {{ form.url_portifolio.label_tag }}
            {{ form.url_portifolio }}
            <div class="invalid-feedback">
                Por favor, insira uma URL válida.
            </div>
        </div>
        <div class="mb-3">
            {{ form.imagem.label_tag }}
            {{ form.imagem }}
            <div class="invalid-feedback">
                Por favor, selecione uma imagem válida.
            </div>
        </div>
        <div class="mb-3">
            {{ form.habilidades.label_tag }}
            {{ form.habilidades }}
            <div class="invalid-feedback">
                Por favor, selecione pelo menos uma habilidade.
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Salvar</button>
        <a href="{% url 'lista_pessoas' %}" class="btn btn-secondary">Voltar</a>
    </form>
</div>
{% endblock %}
```
---

## **4. URLs**
Configure as URLs no `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('pessoas/', views.PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoas/<int:pk>/', views.PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('pessoas/criar/', views.PessoaCreateView.as_view(), name='criar_pessoa'),
    path('pessoas/<int:pk>/editar/', views.PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/<int:pk>/excluir/', views.PessoaDeleteView.as_view(), name='excluir_pessoa'),
    path('buscar/', views.buscar_pessoa, name='buscar_pessoa'),
]
```
###
```python
# Configurações para arquivos de mídia (upload de usuários)
MEDIA_URL = '/media/'  # URL pública para acessar os arquivos
MEDIA_ROOT = BASE_DIR / 'media'  # Caminho no sistema de arquivos para salvar os arquivos



from django.conf.urls.static import static
from exemplo import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
---

## **5. Funcionalidades Adicionais**
- **Validação de Dados**: 
  - Adicione validação no formulário para garantir que `data_aniversario` não seja no futuro.
  - Valide a URL do portfólio com regex.
  
- **Testes**:
  - Escreva testes para verificar o CRUD e a lógica de idade.
  
- **Deploy**:
  - Configure `MEDIA_ROOT` e `MEDIA_URL` para upload de imagens.
  - Use `django-imagekit` para redimensionar imagens automaticamente.

- **Segurança**:
  - Adicione autenticação (`@login_required` ou `LoginRequiredMixin`).
  - Use `django-crispy-forms` para formulários mais profissionais.

---

## **6. Ideias para Atividades Práticas**
1. **Formulário Interativo**: Peça aos alunos para adicionar um campo de "bio" usando `models.TextField`.
2. **API REST**: Integre com Django REST Framework para criar uma API.
3. **Filtros Avançados**: Implemente filtros por idade ou habilidades usando `django-filter`.

- criar e ver a imagem como salvar

