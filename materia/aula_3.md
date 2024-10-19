### **Exceções e Tratamento de Erros**  

---

### **1. Try-Except: Capturando Erros**  
A estrutura `try-except` é usada para **capturar e tratar exceções** que possam ocorrer durante a execução de um bloco de código. Isso permite que o programa continue rodando, mesmo após encontrar um erro.

**Sintaxe Básica:**
```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
```

- **`try`**: Contém o código que pode gerar uma exceção.  
- **`except`**: Define como o erro será tratado. É possível capturar exceções específicas (como `ZeroDivisionError`) ou genéricas.

**Capturando várias exceções:**
```python
try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

---

### **2. Raise: Levantamento Manual de Exceções**  
O comando `raise` permite que você **levante uma exceção manualmente**. Isso é útil quando você quer interromper a execução ou indicar que algo inesperado aconteceu.

**Exemplo:**
```python
def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
    return "Acesso permitido."

try:
    verificar_idade(15)
except ValueError as e:
    print(f"Erro: {e}")
```

---

### **3. Finally: Ações Finais**  
O bloco `finally` é executado **independentemente de uma exceção ocorrer ou não**. Ele é útil para tarefas que precisam ser feitas em qualquer circunstância, como **fechar arquivos** ou liberar recursos.

**Exemplo:**
```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    arquivo.close()
    print("Arquivo fechado.")
```

---

### **Resumo Final**  
- **try-except**: Captura e trata exceções, evitando a interrupção do programa.  
- **raise**: Levanta exceções manualmente para indicar erros.  
- **finally**: Executa ações finais independentemente do sucesso ou falha do bloco `try`.  