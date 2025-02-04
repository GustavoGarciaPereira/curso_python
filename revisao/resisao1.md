
## **Revisão Geral - Python, POO, MySQL e Frameworks Web**

### **1. Python Básico**
**Conceitos:**
- Tipos de dados: `int`, `float`, `str`, `list`, `dict`, `tuple`, `set`
- Estruturas de controle: `if/elif/else`, `for`, `while`
- Funções: definição, parâmetros, `return`, escopo de variáveis
- Módulos e pacotes: `import`, criação e uso

**Exemplo Prático:**
```python
# Função que calcula média com lista
def calcular_media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

print(calcular_media([7, 8, 9]))  # Saída: 8.0
```

---

### **2. Programação Orientada a Objetos (POO)**
**Conceitos:**
- Classes e objetos
- Métodos (incluindo `__init__`, `__str__`)
- Herança e polimorfismo
- Encapsulamento (atributos privados com `_` ou `__`)
- Propriedades (`@property`, setters)

**Exemplo Prático:**
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"

meu_pet = Cachorro("Rex")
print(meu_pet.emitir_som())  # Saída: Au Au!
```

---

### **3. MySQL Básico**
**Conceitos:**
- CRUD: `CREATE`, `SELECT`, `UPDATE`, `DELETE`
- Joins: `INNER JOIN`, `LEFT JOIN`
- Constraints: `PRIMARY KEY`, `FOREIGN KEY`
- Normalização de dados

**Exemplo de Query:**
```sql
-- Criar tabela 'clientes'
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Consulta com WHERE
SELECT * FROM clientes WHERE nome LIKE 'A%';
```

---

### **4. Integração Python + MySQL**
**Conceitos:**
- Uso do `mysql-connector-python`
- Gerenciamento de conexões e cursors
- Prevenção de SQL injection

**Exemplo Prático:**
```python
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha",
    database="empresa"
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

cursor.close()
conexao.close()
```

---

### **5. Django (Framework Web)**
**Conceitos:**
- Estrutura MVT (Model-View-Template)
- ORM do Django
- Rotas (`urls.py`)
- Templates com Django Template Language
- Formulários e validação

**Exemplo de Model:**
```python
# models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome
```

---

### **6. Flask (Microframework)**
**Conceitos:**
- Rotas com `@app.route`
- Templates Jinja2
- Uso de extensões (`Flask-SQLAlchemy`, `Flask-WTF`)
- Requisições e respostas

**Exemplo Prático:**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao meu site!"

@app.route('/usuario/<nome>')
def usuario(nome):
    return f"Olá, {nome}!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

### **7. Comparação Django vs Flask**
| **Característica**       | **Django**                          | **Flask**               |
|--------------------------|-------------------------------------|-------------------------|
| Tipo                      | Framework Full-Stack                | Microframework          |
| Banco de Dados            | ORM Integrado                       | Usa extensões (ex: SQLAlchemy) |
| Complexidade              | Mais estruturado                    | Mais flexível           |
| Aprendizado               | Curva mais íngreme                  | Mais simples para iniciantes |
| Casos de Uso              | Aplicações complexas (ex: e-commerce) | APIs e apps simples |

---

### **8. Exercícios de Revisão**
1. Crie uma classe `ContaBancaria` com métodos para depósito e saque.
2. Escreva uma query SQL para listar pedidos feitos em janeiro/2024.
3. Crie uma rota em Flask que retorne JSON com dados de um produto.
4. No Django, crie um formulário para cadastro de usuários.
5. Converta um dicionário Python em uma tabela MySQL usando o connector.
