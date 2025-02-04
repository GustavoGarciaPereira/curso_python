from produto.models import Produto


produtos = Produto.objects.filter(ativo=False)

for i in produtos:
    print(i.ativo)
    i.ativo = True
    i.save()


