class ContextoPersonalizado:
    def __enter__(self):
        print("Iniciando o contexto...")
        return range(10)  # Retornamos o range como parte do contexto

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto...")

# Usando o `with` com a classe `ContextoPersonalizado`
with ContextoPersonalizado() as numeros:
    for numero in numeros:
        print(numero)
