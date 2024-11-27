from produto.models import Produto

def main():
    produto = Produto.objects.all()


    for i in produto:
        print(f"{i.nome} - {i.preco} - {i.descricao}")
    
    
if __name__ == "__main__":
    main()