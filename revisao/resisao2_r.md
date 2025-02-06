### **Soluções Sugeridas** 

**1. Verificador de Palíndromo:**
```python
def eh_palindromo(texto):
    texto_formatado = texto.replace(" ", "").lower()
    return texto_formatado == texto_formatado[::-1]
```

**2. Segundo Maior Número:**
```python
def segundo_maior(lista):
    valores_unicos = list(set(lista))
    valores_unicos.sort()
    return valores_unicos[-2] if len(valores_unicos) >= 2 else None
```

**3. Contador de Letras:**
```python
def contar_letras(texto):
    contagem = {}
    for letra in texto.lower():
        if letra.isalpha():
            contagem[letra] = contagem.get(letra, 0) + 1
    return contagem
```

**4. Filtro de Números Primos:**
```python
def numeros_primos(n):
    primos = []
    for num in range(2, n + 1):
        eh_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos
```

**5. Inversor de Dicionário:**
```python
def inverter_dicionario(dicionario):
    invertido = {}
    for chave, valor in dicionario.items():
        if valor in invertido:
            invertido[valor].append(chave)
        else:
            invertido[valor] = [chave]
    return invertido
```