---

### Questionário: Orientação a Objetos em Python
---

#### 1. O que é Programação Orientada a Objetos (POO)?
a) Um paradigma de programação que utiliza funções puras.  
b) Um paradigma de programação que organiza o software em objetos que contêm dados e comportamentos.  
c) Uma metodologia para desenvolvimento de software baseada em documentação extensiva.  
d) Nenhuma das alternativas acima.

---

#### 2. Em Python, como se define uma classe chamada `Animal`?

a)
```python
class Animal:
    pass
```

b)
```python
def Animal:
    pass
```

c)
```python
class Animal():
```

d) Todas as alternativas acima estão corretas.

---

#### 3. O que é um objeto em POO?

a) Uma função que realiza uma tarefa específica.  
b) Uma instância de uma classe que possui atributos e métodos.  
c) Um tipo de dado primitivo.  
d) Nenhuma das alternativas acima.

---

#### 4. Qual método especial é chamado quando uma nova instância de uma classe é criada?

a) `__str__`  
b) `__init__`  
c) `__new__`  
d) `__start__`

---

#### 5. Verdadeiro ou Falso: Em Python, uma classe pode herdar de múltiplas classes base.

a) Verdadeiro  
b) Falso

---

#### 6. O que é encapsulamento em POO?

a) O processo de esconder os detalhes internos de uma classe e expor apenas o necessário.  
b) A capacidade de uma classe herdar atributos e métodos de outra classe.  
c) A habilidade de métodos com o mesmo nome se comportarem de maneiras diferentes.  
d) Nenhuma das alternativas acima.

---

#### 7. Como você cria um método que não recebe acesso ao objeto ou à classe dentro de uma classe em Python?

a) Usando `@staticmethod`  
b) Usando `@classmethod`  
c) Definindo o método sem `self` como parâmetro  
d) Ambas a e c estão corretas.

---

#### 8. O que é polimorfismo em POO?

a) A capacidade de uma classe ter múltiplas formas ou comportamentos diferentes.  
b) A habilidade de uma classe herdar atributos de outra classe.  
c) O ato de esconder os dados internos de uma classe.  
d) Nenhuma das alternativas acima.

---

#### 9. Qual a saída do seguinte código?

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Pessoa: {self.nome}"

p = Pessoa("Ana")
print(p)
```

a) `<__main__.Pessoa object at 0x...>`  
b) `Pessoa: Ana`  
c) `Ana`  
d) Erro de execução

---

#### 10. Como você sobrescreve (override) um método da classe pai em uma classe filha?

a) Definindo um método com o mesmo nome na classe filha.  
b) Usando o método `super()`.  
c) Não é possível sobrescrever métodos em Python.  
d) Usando a palavra-chave `override`.

---

#### 11. Qual a diferença entre `@staticmethod` e `@classmethod`?

a) `@staticmethod` pode acessar a classe, enquanto `@classmethod` não pode.  
b) `@classmethod` recebe a classe como primeiro parâmetro (`cls`), enquanto `@staticmethod` não recebe nenhum parâmetro especial.  
c) Não há diferença, ambos funcionam da mesma forma.  
d) `@staticmethod` só pode ser usado em funções de utilidade.

---

#### 12. Verdadeiro ou Falso: Em Python, todos os atributos de uma classe são públicos por padrão.

a) Verdadeiro  
b) Falso

---

#### 13. O que é uma propriedade (property) em Python e como ela é utilizada?

a) Uma função que age como um atributo, permitindo controle sobre o acesso e modificação de atributos privados.  
b) Uma variável global acessível em todas as classes.  
c) Um método especial que é chamado automaticamente quando um objeto é destruído.  
d) Nenhuma das alternativas acima.

---

#### 14. Dê um exemplo de herança múltipla em Python.

Resposta:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

class Aquatico:
    def nadar(self):
        print("Estou nadando.")

class Baleia(Animal, Aquatico):
    def __init__(self, nome, tamanho):
        Animal.__init__(self, nome)
        self.tamanho = tamanho

    def exibir_info(self):
        print(f"{self.nome} tem {self.tamanho} metros de comprimento.")

# Exemplo de uso
baleia = Baleia("Baleia Azul", 30)
baleia.exibir_info()
baleia.comer()
baleia.nadar()
```

---

#### 15. Explique o conceito de "método abstrato" e como implementá-lo em Python.

Resposta:

Métodos abstratos são métodos declarados em uma classe base que não possuem implementação. Eles obrigam as classes derivadas a implementar esses métodos, garantindo que certas funcionalidades sejam definidas nas subclasses.

Para implementar métodos abstratos em Python, utiliza-se o módulo `abc` e o decorador `@abstractmethod`.

Exemplo:

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Tentativa de instanciar Forma resultará em erro
# forma = Forma()  # TypeError

retangulo = Retangulo(5, 10)
print(retangulo.area())  # Saída: 50
```

---

#### 16. O que são métodos mágicos (dunder methods) em Python? Dê dois exemplos.

Resposta:

Métodos mágicos, também conhecidos como "dunder methods" (double underscore), são métodos especiais pré-definidos em Python que começam e terminam com dois underscores. Eles permitem a sobrecarga de operações padrão e a personalização do comportamento das classes.

Exemplos:

1. `__init__(self, ...)`: Método construtor chamado ao criar uma nova instância da classe.
2. `__str__(self)`: Define a representação em string do objeto, usada pela função `print()`.

---

#### 17. Como implementar a sobrecarga de operadores em uma classe Python?

Resposta:

A sobrecarga de operadores em Python é implementada definindo métodos mágicos correspondentes aos operadores desejados na classe. Por exemplo, para sobrecarregar o operador de adição (`+`), define-se o método `__add__`.

Exemplo:

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
p3 = p1 + p2
print(p3)  # Saída: Ponto(4, 6)
```

---

#### 18. Qual é a finalidade do método `__repr__` em uma classe Python?

a) Fornecer uma representação informal e legível para humanos do objeto.  
b) Fornecer uma representação oficial que pode ser usada para recriar o objeto.  
c) Ambas a e b estão corretas.  
d) Nenhuma das alternativas acima.

---

#### 19. O que acontece se você não definir o método `__init__` em uma classe Python?

a) A classe não pode ser instanciada.  
b) A classe terá um método `__init__` padrão que não faz nada.  
c) Todos os objetos terão atributos não inicializados.  
d) Um erro será lançado durante a definição da classe.

---

#### 20. Diferencie composição e agregação em POO com exemplos em Python.

Resposta:

Composição e agregação são dois tipos de relações entre classes em POO que descrevem como as classes se relacionam entre si.

- Composição: Representa uma relação "tem-um" forte onde a vida do objeto dependente está ligada à vida do objeto principal. Se o objeto principal for destruído, os objetos dependentes também são.

Exemplo de Composição:

```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, motor_tipo):
        self.motor = Motor(motor_tipo)

# Uso
carro = Carro("V8")
print(carro.motor.tipo)  # Saída: V8
```

- Agregação: Representa uma relação "tem-um" fraca onde os objetos podem existir independentemente uns dos outros.

Exemplo de Agregação:

```python
class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

# Uso
aluno1 = Aluno("João")
aluno2 = Aluno("Maria")

curso = Curso("Matemática")
curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

print([aluno.nome for aluno in curso.alunos])  # Saída: ['João', 'Maria']
```
