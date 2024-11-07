class RangeContexto:
    def __init__(self, n):
        self.n = n
    
    def __enter__(self):
        # Retorna o range como parte do contexto
        return range(self.n)

    def __exit__(self, exc_type, exc_value, traceback):
        # Nada específico a ser feito ao sair, mas poderíamos colocar uma limpeza aqui
        pass

# Usando o `with` com a classe `RangeContexto`
with RangeContexto(10) as numeros:
    for numero in numeros:
        print(numero)
