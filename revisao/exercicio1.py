# def eh_palindromo(palavra):
#     m_palavra = palavra.lower()
#     return m_palavra == m_palavra[::-1]



# print(eh_palindromo("Ana"))      # Saída: True
# print(eh_palindromo("ana"))      # Saída: True
# print(eh_palindromo("Python"))   # Saída: False

# def segundo_maior(numeros:list):
#     numeros.sort(reverse=True)
#     return numeros[1]


# print(segundo_maior([3, 5, 1, 8, 10]))  # Saída: 8
# print(segundo_maior([-10, 0, -5]))      # Saída: -5


# def contar_letras(palavra):
#     res_dic = dict()

#     for L in palavra:
#         res_dic[L] = res_dic.get(L,0) + 1

#     return res_dic

# print(contar_letras("programação")) 
# # Saída: {'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 2, 'm': 1, 'ç': 1, 'ã': 1}


class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(f"seu saldo é de R${self.saldo}")
    def sacar(self, valor):
        if valor < 0:
            print("valor menor que zero")
            return
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("valor Insuficiente")

conta = ContaBancaria()
conta.deposito(100)
conta.mostrar_saldo()
conta.deposito(100)
conta.mostrar_saldo()
conta.sacar(-1)
conta.mostrar_saldo()
