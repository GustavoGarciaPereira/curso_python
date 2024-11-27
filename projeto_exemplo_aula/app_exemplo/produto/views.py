from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Listar produtos
from django.db.models import Q  # Para buscas mais complexas

from django.shortcuts import render
from .models import Produto

def produto_list(request):
    query = request.GET.get('q', '')  # Obter valor da busca
    order = request.GET.get('order', '')  # Obter parâmetro de ordenação

    # Filtrar produtos
    produtos = Produto.objects.all()
    if query:
        produtos = produtos.filter(nome__icontains=query)

    # Ordenar produtos
    if order == 'nome':
        produtos = produtos.order_by('nome')
    elif order == 'preco':
        produtos = produtos.order_by('preco')

    return render(request, 'produto_list.html', {'produtos': produtos, 'query': query})

# Detalhar produto
def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produto_detail.html', {'produto': produto})

# Criar novo produto
def produto_create(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})

# Editar produto
def produto_edit(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})

# Excluir produto
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})
