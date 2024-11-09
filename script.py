

def pessoa_media(nome, nt1, nt2):
    
    media = (nt1 + nt2) / 2
    return nome, media, "asdfasdf"

dic = {
    "nome": "gustavo",
    "nt1": 8.5,
    "nt2": 9.0
}

print(pessoa_media(**dic))