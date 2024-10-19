## **Resumo: Controle de Fluxo em Python**  

### **Estruturas Condicionais: `if`, `elif`, `else`**  
As **estruturas condicionais** são usadas para controlar o fluxo do programa com base em condições.

- **`if`**: Avalia uma condição e executa o bloco correspondente se for **verdadeira**.
- **`elif`**: Permite testar múltiplas condições. Executa o bloco quando a primeira condição verdadeira é encontrada.
- **`else`**: Executa um bloco se todas as condições anteriores forem **falsas**.

**Exemplo:**
```python
x = 10

if x > 20:
    print("Maior que 20")
elif x > 5:
    print("Entre 6 e 20")  # Executa este bloco
else:
    print("5 ou menor")
```

---

### **Loops: `for` e `while`**  

#### **`for` Loop**  
- Executa um bloco de código **para cada item** em uma sequência (lista, tupla, string, etc.).
- Útil para **iterações conhecidas** de antemão.

**Exemplo:**
```python
for i in range(5):
    print(i)  # Saída: 0, 1, 2, 3, 4
```

#### **`while` Loop**  
- Repete o bloco de código **enquanto uma condição for verdadeira**.
- Ideal para situações em que o número de repetições não é conhecido previamente.

**Exemplo:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Saída: 0, 1, 2, 3, 4
```

---

### **Uso de `break`, `continue` e `else` em Loops**  

- **`break`**: Encerra o loop imediatamente, independente das condições futuras.  
  **Exemplo:**
  ```python
  for i in range(10):
      if i == 5:
          break  # Interrompe o loop quando i é 5
      print(i)  # Saída: 0, 1, 2, 3, 4
  ```

- **`continue`**: Pula a iteração atual e vai para a **próxima**.
  **Exemplo:**
  ```python
  for i in range(5):
      if i == 2:
          continue  # Pula o número 2
      print(i)  # Saída: 0, 1, 3, 4
  ```

- **`else` em Loops**: O bloco **else** é executado se o loop **não for interrompido por um `break`**.  
  **Exemplo:**
  ```python
  for i in range(5):
      if i == 3:
          break
  else:
      print("Loop completo")  # Não será executado

  while False:
      pass
  else:
      print("While não entrou no loop")  # Saída: While não entrou no loop
  ```

---