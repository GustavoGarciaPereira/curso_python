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
