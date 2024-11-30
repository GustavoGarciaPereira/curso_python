from django.shortcuts import get_object_or_404, redirect, render
from produto.models import Produto
# Create your views here.
def listagem_ativo(request):
    ativo = Produto.objects.filter(ativo=True)
    return render(request, 'ativo.html',{'ativo':ativo})


def listagem_nao_ativo(request):
    nao_ativo = Produto.objects.filter(ativo=False)
    return render(request, 'listagem_nao_ativo.html',{"nao_ativo":nao_ativo})


def reativar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    print("produto",request.method)
    if request.method == "POST":
        print("||produto",produto)
        produto.ativo = True  # Desativar o produto
        produto.save()  # Salvar a alteração no banco de dados
        return redirect('nao_ativo')
    return render(request, 'confim.html',{"nao_ativo":produto})

