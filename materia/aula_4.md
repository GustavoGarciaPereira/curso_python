## **Resumo: Estruturas de Dados Avançadas**  

### **Filas e Pilhas usando Listas ou Deque**  
- **Pilha (Stack)**:  
  - Estrutura do tipo **LIFO** (Last In, First Out).
  - Exemplo: pilha de pratos (o último prato a entrar é o primeiro a sair).
  - Em Python:
    - Usando **lista**: `append()` para inserir e `pop()` para remover.
    ```python
    pilha = []
    pilha.append(1)  # Inserir
    pilha.pop()       # Remover
    ```
    - Usando **deque** (da biblioteca `collections`): mais eficiente para grandes volumes.
    ```python
    from collections import deque
    pilha = deque()
    pilha.append(1)  
    pilha.pop()  
    ```

- **Fila (Queue)**:  
  - Estrutura do tipo **FIFO** (First In, First Out).
  - Em Python:
    - Usando **lista**: pouco eficiente para remoção no início.
    ```python
    fila = [1, 2, 3]
    fila.pop(0)  # Remover o primeiro elemento
    ```
    - Usando **deque**: mais rápido para inserção e remoção nas extremidades.
    ```python
    fila = deque([1, 2, 3])
    fila.append(4)   # Inserir no final
    fila.popleft()   # Remover do início
    ```

### **Dicionários Aninhados e Manipulação Avançada**  
- Dicionários aninhados são úteis para representar estruturas hierárquicas.  
  Exemplo: dados de clientes organizados por cidade e nome.
  ```python
  clientes = {
      "São Paulo": {"Carlos": {"idade": 30, "compra": 250.0}},
      "Rio": {"Ana": {"idade": 22, "compra": 320.0}}
  }
  # Acessar informações
  print(clientes["São Paulo"]["Carlos"]["idade"])  # Saída: 30
  ```

- **Manipulação Avançada**:
  - Atualização de valores:
    ```python
    clientes["Rio"]["Ana"]["compra"] += 50
    ```
  - Percorrer um dicionário aninhado:
    ```python
    for cidade, pessoas in clientes.items():
        for nome, info in pessoas.items():
            print(f"{nome} de {cidade} fez uma compra de {info['compra']}")
    ```

### **Compreensão de Listas, Dicionários e Conjuntos**  
- **Compreensão de Lista (List Comprehension)**:  
  Uma forma concisa e eficiente de criar listas.
  ```python
  pares = [x for x in range(10) if x % 2 == 0]
  print(pares)  # Saída: [0, 2, 4, 6, 8]
  ```

- **Compreensão de Dicionário**:
  ```python
  quadrados = {x: x**2 for x in range(5)}
  print(quadrados)  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

- **Compreensão de Conjuntos (Set Comprehension)**:
  ```python
  conjunto = {x for x in "abracadabra" if x not in "abc"}
  print(conjunto)  # Saída: {'d', 'r'}
  ```