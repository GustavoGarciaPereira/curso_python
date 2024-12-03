import requests
import random
from decimal import Decimal
def calcular_frete(cep_origem, cep_destino, peso, comprimento, altura, largura, servico="sedex"):
    """
    Consome uma API externa para calcular o custo do frete.

    Args:
        cep_origem (str): CEP de origem.
        cep_destino (str): CEP de destino.
        peso (float): Peso do pacote em kg.
        comprimento (float): Comprimento do pacote em cm.
        altura (float): Altura do pacote em cm.
        largura (float): Largura do pacote em cm.
        servico (str): Tipo de serviço (ex.: sedex ou pac).

    Returns:
        dict: Resultado da API ou valor aleatório em caso de erro.
    """
    url = "https://api.frete.com/v1/calculate"  # URL fictícia para API de frete
    payload = {
        "cep_origem": cep_origem,
        "cep_destino": cep_destino,
        "peso": peso,
        "comprimento": comprimento,
        "altura": altura,
        "largura": largura,
        "servico": servico
    }
    headers = {"Content-Type": "application/json"}  # Cabeçalhos (se necessário)

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Levanta exceção para erros HTTP

        # Verifica se a API retornou o valor esperado
        data = response.json()
        if "valor" in data:
            return {"valor": data["valor"]}
        else:
            raise ValueError("Resposta inesperada da API")

    except (requests.exceptions.RequestException, ValueError) as e:
        # Retorna um valor aleatório entre 20 e 100 em caso de erro
        valor_randomico = random.uniform(20, 100)
        return {"valor": round(Decimal(valor_randomico),2), "erro": f"Erro ao consultar frete: {e}"}



def servico_ia_tags(nome_produto, descricao_produto):
    # Endpoint da API
    url = "https://api.perplexity.ai/chat/completions"

    # Substitua pelo seu token de autorização
    token = "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"

    # Dados do produto
    # nome_produto = "Notebook XYZ"
    # descricao_produto = "Notebook de alto desempenho com processador Intel Core i7, 16GB de RAM, SSD de 512GB e tela Full HD de 15,6 polegadas."

    # Payload ajustado para gerar tags baseadas no texto do produto
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",  # Certifique-se de que o modelo seja o mais adequado
        "messages": [
            {
                "role": "system",
                "content": "Generate concise and relevant tags for projects based on the given product description."
            },
            {
                "role": "user",
                "content": f"Product Name: {nome_produto}\nDescription: {descricao_produto}\n\nGenerate relevant project tags."
            }
        ],
        "max_tokens": 50,
        "temperature": 0.2,
        "top_p": 0.9,
        "search_domain_filter": [],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }

    # Cabeçalhos
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Chamada para a API
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        content = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        
        # Processar a resposta para obter uma lista de tags limpas
        tags = content.split("\n")  # Quebra por linhas
        tags = [
            tag.lstrip("- 1234567890.").strip("**").strip()  # Remove prefixos como "-", números e "**"
            for tag in tags if tag.strip()
        ]
        return tags[1:]
    return []



# from produto.models import Produto

# import json

# produto = Produto.objects.get(id=16)

# for produto in produtos:
#     if isinstance(produto.tags, str):
#         try:
#             # Processar string para extrair as tags
#             tags = produto.tags.split("\n")
#             tags = [tag.lstrip("1234567890. ").strip("**").strip() for tag in tags if tag.strip()]
#             produto.tags = tags
#             produto.save()
#         except Exception as e:
#             print(f"Erro ao processar produto {produto.id}: {e}")


# tags = produto.tags[0].split("\n")
# tags = [tag.lstrip("1234567890. ").strip("**").strip() for tag in tags if tag.strip()]
# produto.tags = tags
# produto.save()