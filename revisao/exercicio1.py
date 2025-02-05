# def eh_palindromo(palavra):
#     m_palavra = palavra.lower()
#     return m_palavra == m_palavra[::-1]



# print(eh_palindromo("Ana"))      # Saída: True
# print(eh_palindromo("ana"))      # Saída: True
# print(eh_palindromo("Python"))   # Saída: False

def segundo_maior(numeros:list):
    numeros.sort()
    return numeros


print(segundo_maior([3, 5, 1, 8, 10]))  # Saída: 8
print(segundo_maior([-10, 0, -5]))      # Saída: -5