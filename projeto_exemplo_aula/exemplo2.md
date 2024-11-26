### Desenvolvimento dos Modelos e Funcionalidades

Aqui está o desenvolvimento completo com exemplos de modelos, relacionamentos, configuração no admin e integração com formulários.

---

### **1. Modelos com Relacionamentos**

Vamos expandir o modelo `Produto` para incluir relacionamentos `One-to-Many` e `Many-to-Many`.

**Arquivo: `produtos/models.py`**
```python
from django.db import models

# Categoria: Um Produto pertence a uma Categoria (One-to-Many)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Fornecedor: Um Produto pode ter vários Fornecedores (Many-to-Many)
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

# Produto: Relaciona-se com Categoria e Fornecedor
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedores = models.ManyToManyField(Fornecedor)

    def __str__(self):
        return f"{self.nome} ({self.categoria})"
```

#### Explicação:
1. **`Categoria`**: Representa uma categoria. Um produto pertence a apenas uma categoria.
2. **`Fornecedor`**: Representa fornecedores. Um produto pode ter vários fornecedores, e um fornecedor pode fornecer vários produtos.
3. **`Produto`**: Inclui relações `ForeignKey` para `Categoria` e `ManyToManyField` para `Fornecedor`.

---

### **2. Registro no Admin do Django**

**Arquivo: `produtos/admin.py`**
```python
from django.contrib import admin
from .models import Categoria, Fornecedor, Produto

# Registrando as categorias
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# Registrando os fornecedores
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')

# Registrando os produtos
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    filter_horizontal = ('fornecedores',)
```

#### Recursos do Admin:
1. **`list_display`**: Mostra as colunas na listagem.
2. **`search_fields`**: Adiciona barra de pesquisa.
3. **`list_filter`**: Filtros na barra lateral.
4. **`filter_horizontal`**: Interface amigável para campos `Many-to-Many`.

---

### **3. Integração com Formulários**

#### **3.1. Formulários Baseados em Modelos**

**Arquivo: `produtos/forms.py`**
```python
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'categoria', 'fornecedores']
```

#### **3.2. Criação de Views e Templates**

**Arquivo: `produtos/views.py`**
```python
from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

# Lista de produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

# Criar ou editar produto
def editar_produto(request, produto_id=None):
    if produto_id:
        produto = Produto.objects.get(id=produto_id)
    else:
        produto = None

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/editar_produto.html', {'form': form})
```

---

#### **3.3. Templates**

**Template: `produtos/lista_produtos.html`**
```html
<h1>Lista de Produtos</h1>
<a href="{% url 'editar_produto' %}">Adicionar Produto</a>
<table>
    <thead>
        <tr>
            <th>Nome</th>
            <th>Preço</th>
            <th>Estoque</th>
            <th>Categoria</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        {% for produto in produtos %}
        <tr>
            <td>{{ produto.nome }}</td>
            <td>{{ produto.preco }}</td>
            <td>{{ produto.estoque }}</td>
            <td>{{ produto.categoria }}</td>
            <td>
                <a href="{% url 'editar_produto' produto.id %}">Editar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Template: `produtos/editar_produto.html`**
```html
<h1>{% if form.instance.id %}Editar Produto{% else %}Adicionar Produto{% endif %}</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Salvar</button>
</form>
```

---

### **4. URLs**

**Arquivo: `produtos/urls.py`**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('novo/', views.editar_produto, name='novo_produto'),
]
```

**Arquivo: `minha_loja/urls.py`**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
]
```

---

### **5. Testando no Navegador**
1. Acesse `http://127.0.0.1:8000/produtos/` para listar os produtos.
2. Clique em "Adicionar Produto" para criar um novo.
3. Edite ou exclua produtos conforme necessário.

---

### **Resumo**
- Criamos modelos com relacionamentos `One-to-Many` e `Many-to-Many`.
- Configuramos o Django Admin para gerenciar os dados.
- Criamos formulários baseados em modelos para adicionar/editar produtos.
- Montamos views e templates para interagir com os modelos.