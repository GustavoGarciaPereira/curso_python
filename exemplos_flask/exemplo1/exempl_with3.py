#sem with
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()  # Aqui, o fechamento precisa ser manual



#com with
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# O arquivo é fechado automaticamente aqui, ao final do bloco `with`
