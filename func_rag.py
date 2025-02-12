from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import json

def rag_function_perplexity(user_query, documents, perplexity_api_key):
    """
    Função para implementar um sistema RAG (Retrieval-Augmented Generation) básico
    usando a API da Perplexity AI com o modelo llama-3.1-sonar-small-128k-online.

    Args:
        user_query (str): A pergunta do usuário.
        documents (list): Uma lista de strings representando os documentos a serem usados como base de conhecimento.
        perplexity_api_key (str): Sua chave de API da Perplexity AI.

    Returns:
        str: A resposta gerada pelo modelo de linguagem da Perplexity AI, baseada nos documentos relevantes.
               Retorna uma mensagem de erro em caso de falha na geração da resposta.
    """
    try:
        # 1. Embedding dos Documentos e da Query
        model = SentenceTransformer('distilbert-multilingual-nli-stsb-quora-dir') # Modelo Sentence Transformer para embeddings multilingue

        document_embeddings = model.encode(documents) # Cria embeddings para cada documento
        query_embedding = model.encode(user_query) # Cria embedding para a pergunta do usuário

        # 2. Encontrar Documentos Relevantes (Similaridade por Cosseno)
        similarity_scores = cosine_similarity([query_embedding], document_embeddings)[0] # Calcula a similaridade do cosseno entre a query e cada documento

        # Ordena os documentos por similaridade e pega os mais relevantes (ex: top 3)
        document_similarity_pairs = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)
        top_document_indices = [index for index, score in document_similarity_pairs[:min(3, len(documents))]] # Pega os índices dos 3 documentos mais similares ou menos se houver menos de 3 documentos

        relevant_documents = [documents[index] for index in top_document_indices] # Recupera os documentos relevantes

        # 3. Criar Prompt para o Modelo de Linguagem
        context = "\n".join(relevant_documents) # Junta os documentos relevantes em um único contexto

        prompt_content = f"Responda à seguinte pergunta com base no contexto fornecido. \n\nContexto:\n{context}\n\nPergunta:\n{user_query}\n\nResposta:" # Cria o prompt formatado

        # 4. Interação com o Modelo de Linguagem (Perplexity AI API - llama-3.1-sonar-small-128k-online)
        url = "https://api.perplexity.ai/chat/completions"

        payload = json.dumps({ # Converte o payload para JSON string
            "model": "llama-3.1-sonar-small-128k-online", # Modelo Perplexity AI a ser usado
            "messages": [
                {
                    "role": "system",
                    "content": "Be precise and concise." # Instrução de sistema (opcional)
                },
                {
                    "role": "user",
                    "content": prompt_content # Usa o prompt formatado com contexto e pergunta
                }
            ],
             "max_tokens": 500, # Aumentei o max_tokens para permitir respostas mais longas se necessário
            "temperature": 0.2, # Mantive a temperatura baixa para respostas mais determinísticas
            "top_p": 0.9, # Mantive o top_p
        })
        headers = {
            "Authorization": f"Bearer {perplexity_api_key}", # Usa a chave de API passada como argumento
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers) # Faz a requisição POST para a API da Perplexity AI
        response_json = response.json() # Converte a resposta JSON para um dicionário Python

        if 'choices' in response_json and response_json['choices']: # Verifica se a resposta contém escolhas
            response_text = response_json['choices'][0]['message']['content'] # Extrai o texto da resposta
        else:
            return "Erro ao obter resposta da Perplexity AI API." # Retorna mensagem de erro se a resposta não tiver o formato esperado


        return response_text # Retorna a resposta gerada

    except Exception as e:
        return f"Ocorreu um erro ao processar a requisição: {e}" # Retorna mensagem de erro em caso de exceção

# Exemplo de uso da função (para testes fora do Django)
if __name__ == '__main__':
    documentos_exemplo = [
        "A Torre Eiffel é um monumento de treliça de ferro forjado no Champ de Mars em Paris, França.",
        "Foi nomeada em homenagem ao engenheiro Gustave Eiffel, cuja empresa projetou e construiu a torre.",
        "Construída em 1889 como entrada para a Feira Mundial de 1889, foi inicialmente criticada por alguns artistas e intelectuais franceses pelo seu design, mas tornou-se um ícone cultural global da França e uma das estruturas mais reconhecidas do mundo."
    ]
    pergunta_usuario = "Quando a Torre Eiffel foi construída e quem a projetou?"

    # **IMPORTANTE:** Substitua 'SUA_CHAVE_API_PERPLEXITY' pela sua chave de API real da Perplexity AI
    api_key_perplexity = "SUA_CHAVE_API_PERPLEXITY" # <----------------------- Substitua aqui!

    resposta_rag = rag_function_perplexity(pergunta_usuario, documentos_exemplo, api_key_perplexity)
    print(f"Pergunta do Usuário: {pergunta_usuario}")
    print(f"Resposta do RAG (Perplexity):\n{resposta_rag}")
