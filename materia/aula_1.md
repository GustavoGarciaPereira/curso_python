**operadores lógicos, variáveis e operadores aritméticos** em Python:

---

## 1. Operadores Lógicos  
Os operadores lógicos são usados para combinar expressões e produzir resultados booleanos (**True** ou **False**). 

- **and**: Retorna `True` se **ambas** as condições forem verdadeiras.  
  ```python
  print(True and False)  # False
  ```
  
- **or**: Retorna `True` se **pelo menos uma** condição for verdadeira.  
  ```python
  print(True or False)  # True
  ```

- **not**: Inverte o valor lógico da expressão.  
  ```python
  print(not True)  # False
  ```

---

## 2. Variáveis  
As variáveis armazenam valores na memória para serem usados ao longo do programa. Elas não precisam ser declaradas com tipos específicos em Python (linguagem de tipagem dinâmica).

### Declaração e atribuição:
```python
x = 5       # Inteiro
y = 3.14    # Ponto flutuante
name = "Gustavo"  # String
is_active = True  # Booleano
```

- **Regras para variáveis:**
  - Devem começar com uma letra ou sublinhado (_).
  - Não podem conter espaços nem começar com números.
  - Devem ser escritas de forma clara e descritiva para facilitar a leitura do código.

---

## 3. Operadores Aritméticos  
Os operadores aritméticos realizam operações matemáticas básicas.

- **+**: Adição  
  ```python
  print(5 + 3)  # 8
  ```

- **-**: Subtração  
  ```python
  print(10 - 4)  # 6
  ```

- **\***: Multiplicação  
  ```python
  print(7 * 3)  # 21
  ```

- **/**: Divisão (resultado sempre ponto flutuante)  
  ```python
  print(10 / 3)  # 3.3333...
  ```

- **//**: Divisão inteira (descarta a parte decimal)  
  ```python
  print(10 // 3)  # 3
  ```

- **%**: Módulo (resto da divisão)  
  ```python
  print(10 % 3)  # 1
  ```

- **\*\***: Exponenciação (potência)  
  ```python
  print(2 ** 3)  # 8
  ```

---