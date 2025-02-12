# views.py (exemplo básico - atualizado para Perplexity)
from django.shortcuts import render
from .rag_function import rag_function_perplexity # Importe a função RAG da Perplexity AI

def minha_view_rag_perplexity(request): # Nome da view atualizado
    if request.method == 'POST':
        user_query = request.POST.get('user_query')
        documentos_fonte = [
            "Documento 1: ... conteúdo do documento 1 ...",
            "Documento 2: ... conteúdo do documento 2 ...",
            "Documento 3: ... conteúdo do documento 3 ..."
        ]
        perplexity_api_key = "SUA_CHAVE_API_PERPLEXITY" # **Configure sua chave API aqui (ou melhor, em variáveis de ambiente)**

        resposta = rag_function_perplexity(user_query, documentos_fonte, perplexity_api_key) # Chama a função RAG da Perplexity

        return render(request, 'template_da_sua_view.html', {'pergunta': user_query, 'resposta_rag': resposta})

    return render(request, 'template_da_sua_view.html')
