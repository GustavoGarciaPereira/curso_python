### Aula Básica: Introdução a ORMs no Django

---

#### **Objetivo da Aula**
- Entender o que é um ORM (Object-Relational Mapping).
- Aprender os conceitos básicos do ORM do Django.
- Realizar operações básicas com o ORM do Django.

---

### **1. O que é um ORM?**
**ORM (Object-Relational Mapping)** é uma técnica que permite interagir com bancos de dados relacionais usando código orientado a objetos. Em vez de escrever SQL diretamente, usamos objetos Python para manipular dados.

#### **Por que usar um ORM?**
- Abstração: Não precisamos lidar diretamente com SQL.
- Produtividade: Operações no banco são mais rápidas de implementar.
- Portabilidade: O código pode ser usado com diferentes bancos de dados.

No Django, usamos o **Django ORM**, que já vem integrado.

---

### **2. Configuração Inicial no Django**

1. **Criação do Projeto Django**  
   ```bash
   django-admin startproject minha_loja
   cd minha_loja
   ```

2. **Criação de um App**  
   ```bash
   python manage.py startapp produtos
   ```

3. **Registrar o App**  
   Adicione `produtos` no `INSTALLED_APPS` do arquivo `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'produtos',
   ]
   ```

4. **Configurar o Banco de Dados**  
   No arquivo `settings.py`, defina o banco de dados. Por padrão, o Django usa SQLite:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / "db.sqlite3",
       }
   }
   ```

---

### **3. Criando Modelos no Django**

No Django, cada modelo representa uma tabela no banco de dados. Vamos criar um modelo simples para produtos.

1. **Definição do Modelo**  
   No arquivo `produtos/models.py`:
   ```python
   from django.db import models

   class Produto(models.Model):
       nome = models.CharField(max_length=100)
       preco = models.DecimalField(max_digits=10, decimal_places=2)
       estoque = models.IntegerField()

       def __str__(self):
           return self.nome
   ```

   - **`CharField`**: Campo de texto.
   - **`DecimalField`**: Número decimal.
   - **`IntegerField`**: Número inteiro.
   - **`__str__`**: Retorna uma representação legível do objeto.

2. **Criar a Migração**  
   ```bash
   python manage.py makemigrations
   ```

3. **Aplicar a Migração**  
   ```bash
   python manage.py migrate
   ```

---

### **4. Trabalhando com o ORM do Django**

#### **Adicionar Dados**
No arquivo `manage.py shell`:
```python
from produtos.models import Produto

# Criar um produto
produto = Produto(nome="Camiseta", preco=49.90, estoque=100)
produto.save()
```

#### **Consultar Dados**
```python
# Todos os produtos
produtos = Produto.objects.all()
for p in produtos:
    print(p.nome, p.preco)

# Filtrar por nome
camisetas = Produto.objects.filter(nome="Camiseta")
print(camisetas)

# Produto único
produto = Produto.objects.get(id=1)
print(produto.nome)
```

#### **Atualizar Dados**
```python
produto = Produto.objects.get(id=1)
produto.preco = 39.90
produto.save()
```

#### **Deletar Dados**
```python
produto = Produto.objects.get(id=1)
produto.delete()
```

---

### **5. Atividade Prática**

1. **Adicionar 3 produtos diferentes no banco de dados.**
2. **Listar todos os produtos e seus preços.**
3. **Atualizar o estoque de um produto.**
4. **Deletar um produto específico.**

---

### **6. Próximos Passos**

- Relacionamentos entre tabelas (One-to-Many, Many-to-Many).
- Uso do Admin do Django para gerenciar dados.
- Integração com formulários para manipular modelos.


### **Material Complementar**
- [Documentação Oficial do Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/models/)
- [Curso Django ORM Básico no YouTube](https://www.youtube.com)