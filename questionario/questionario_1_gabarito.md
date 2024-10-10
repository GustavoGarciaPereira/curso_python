class ErroPersonalizado(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

def verificar_idade(idade):
    if idade < 0:
        raise ErroPersonalizado("A idade não pode ser negativa.")
    elif idade < 18:
        raise ErroPersonalizado("Acesso permitido apenas para maiores de 18 anos.")
    else:
        print("Acesso concedido.")

try:
    idade = int(input("Digite sua idade: "))
    verificar_idade(idade)
except ErroPersonalizado as e:
    print(f"Erro: {e}")
