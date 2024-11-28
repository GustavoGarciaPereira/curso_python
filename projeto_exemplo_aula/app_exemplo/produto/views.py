from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

from django.contrib.auth.decorators import login_required
# Listar produtos
from django.db.models import Q  # Para buscas mais complexas

from django.shortcuts import render
from .models import Produto

from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_superuser  # Garante que o usuário está autenticado


@login_required
def produto_list(request):
    query = request.GET.get('q', '')  # Obter valor da busca
    order = request.GET.get('order', '')  # Obter parâmetro de ordenação

    # Filtrar apenas produtos ativos
    produtos = Produto.objects.filter(ativo=True)
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
    if not request.user.is_authenticated or not request.user.is_superuser:
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
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
# def produto_delete(request, pk):
#     produto = get_object_or_404(Produto, pk=pk)
#     if request.method == "POST":
#         produto.delete()
#         return redirect('produto_list')
#     return render(request, 'produto_confirm_delete.html', {'produto': produto})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.ativo = False  # Desativar o produto
        produto.save()  # Salvar a alteração no banco de dados
        return redirect('produto_list')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})




from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redireciona usuários logados para a página inicial
    success_url = reverse_lazy('produto_list')  # Página para onde o usuário será redirecionado após login



