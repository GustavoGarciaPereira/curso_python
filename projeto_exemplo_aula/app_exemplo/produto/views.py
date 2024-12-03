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



from django.shortcuts import render
from .models import Produto
from .services import calcular_frete, servico_ia_tags  # Simula cálculo de frete (pode ser implementado como no exemplo anterior)


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

    # Adicionar frete ao contexto
    produtos_com_frete = []
    for produto in produtos:
        # Simula o cálculo de frete (você pode integrar com uma API real)
        frete = calcular_frete("01001-000", "02002-000", peso=produto.estoque, comprimento=20, altura=10, largura=15)
        valor_total = produto.preco + frete.get('valor', 0)  # Adiciona o frete ao preço
        produtos_com_frete.append({
            "produto": produto,
            "frete": frete.get('valor', 0),
            "valor_total": valor_total,
        })

    return render(request, 'produto_list.html', {'produtos': produtos_com_frete, 'query': query})


# Detalhar produto
@login_required
def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produto_detail.html', {'produto': produto})

# Criar novo produto
def produto_create(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            # Gerar tags com base nos dados do formulário
            nome_produto = produto.nome
            descricao_produto = produto.descricao
            produto.tags = servico_ia_tags(nome_produto, descricao_produto)
            produto.save()
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


from django.contrib import messages
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.ativo = False  # Desativar o produto
        produto.save()  # Salvar a alteração no banco de dados
        messages.success(request, f"Produto '{produto.nome}' foi desativado.")
        return redirect('produto_list')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})




from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redireciona usuários logados para a página inicial
    success_url = reverse_lazy('produto_list')  # Página para onde o usuário será redirecionado após login



from django.http import JsonResponse
from .services import calcular_frete

def consulta_frete(request):
    """
    View para calcular o frete com base nos dados fornecidos.

    Returns:
        JsonResponse: Resultado do cálculo do frete ou mensagem de erro.
    """
    if request.method == "POST":
        # Dados de exemplo para consulta
        cep_origem = "01001-000"  # Exemplo fixo de CEP de origem
        cep_destino = request.POST.get("cep_destino", "01002-000")
        peso = float(request.POST.get("peso", 1))
        comprimento = float(request.POST.get("comprimento", 20))
        altura = float(request.POST.get("altura", 10))
        largura = float(request.POST.get("largura", 15))

        # Chamada ao serviço de API
        resultado = calcular_frete(cep_origem, cep_destino, peso, comprimento, altura, largura)
        return JsonResponse(resultado)

    return JsonResponse({"erro": "Método não permitido"}, status=405)
