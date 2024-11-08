import requests

url = "https://api.perplexity.ai/chat/completions"

def obter_resumo_noticia():
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "content": "",
                "role": "system"
            },
            {
                "content": """v""",
                "role": "user"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        resumo = response.json().get('choices', [{}])[0].get('message', {}).get('content')
        return resumo
    else:
        return f"Erro: {response.status_code}, {response.text}"

# # Exemplo de uso
# titulo = "Pressionado a cortar gastos, Lula se vê entre desagradar aliados e acalmar mercado"
# link = "https://www.gazetadopovo.com.br/economia/corte-gastos-pressionado-lula-se-ve-entre-desagradar-aliados-e-acalmar-mercado/"
print(obter_resumo_noticia())


