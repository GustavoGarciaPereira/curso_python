from django.shortcuts import render
from produto.models import Produto
# Create your views here.
def listagem_ativo(request):
    ativo = Produto.objects.filter(ativo=True)
    return render(request, 'listagem_ativo.html',{"ativo":ativo})

def listagem_nao_ativo(request):
    nao_ativo = Produto.objects.filter(ativo=False)
    return render(request, 'listagem_nao_ativo.html',{"nao_ativo":nao_ativo})