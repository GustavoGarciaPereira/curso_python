Em Python, **tipos estruturados** são coleções de valores que permitem agrupar vários elementos em uma única estrutura. Eles são úteis para organizar dados complexos e são amplamente usados para manipular e armazenar informações. Abaixo estão os principais tipos estruturados:

---

## 1. **Listas (`list`)**
As listas são coleções **mutáveis** (podem ser alteradas) e ordenadas. Podem conter diferentes tipos de dados.

### Exemplo:
```python
numeros = [1, 2, 3, 4]
mistura = [10, "Gustavo", True]

# Acesso por índice:
print(numeros[0])  # 1

# Modificando um elemento:
numeros[1] = 20
print(numeros)  # [1, 20, 3, 4]

# Adicionando um elemento:
numeros.append(5)  # [1, 20, 3, 4, 5]
```

---

## 2. **Tuplas (`tuple`)**
As tuplas são semelhantes às listas, mas são **imutáveis** (não podem ser alteradas após a criação).

### Exemplo:
```python
coordenadas = (10.0, 20.5)

# Acesso por índice:
print(coordenadas[0])  # 10.0

# Tuplas não permitem modificações:
# coordenadas[1] = 30  # Erro: TypeError
```

---

## 3. **Dicionários (`dict`)**
Os dicionários são coleções de pares **chave-valor**. As chaves são únicas e imutáveis, e os valores podem ser de qualquer tipo.

### Exemplo:
```python
pessoa = {"nome": "Gustavo", "idade": 30, "ativo": True}

# Acesso por chave:
print(pessoa["nome"])  # Gustavo

# Adicionando um novo par:
pessoa["cidade"] = "São Paulo"
print(pessoa)  # {'nome': 'Gustavo', 'idade': 30, 'ativo': True, 'cidade': 'São Paulo'}

# Modificando um valor:
pessoa["idade"] = 31
```

---

## 4. **Conjuntos (`set`)**
Os conjuntos são coleções **não ordenadas** e **não permitem duplicatas**.

### Exemplo:
```python
numeros = {1, 2, 3, 3}  # Duplicatas são removidas
print(numeros)  # {1, 2, 3}

# Adicionando um elemento:
numeros.add(4)
print(numeros)  # {1, 2, 3, 4}

# Removendo um elemento:
numeros.remove(2)
```

---

## 5. **Strings (`str`)**
Embora as strings sejam frequentemente tratadas como tipos primitivos, elas também são **sequências** de caracteres e podem ser manipuladas como estruturas ordenadas.

### Exemplo:
```python
texto = "Hello, Python!"

# Acesso por índice:
print(texto[0])  # H

# Fatiamento:
print(texto[7:13])  # Python

# Strings são imutáveis:
# texto[0] = 'h'  # Erro: TypeError
```

---