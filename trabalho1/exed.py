



def media_aluno(nome, nota1, nota2, nota3, add):
    
    media  = (nota1 + nota2 + nota3)/3
    
    
    return nome, media, add


dic_info = {
    "nome": "gustavo",
    "nota1": 10,
    "nota2": 3,
    "nota3": 1
}



res = media_aluno(**dic_info, add="as")


print(res)