import requests

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "How many stars are there in our galaxy?"
        }
    ],
    "max_tokens": 100,  # Substitua "Optional" por um número inteiro, como 100
    "temperature": 0.2,
    "top_p": 0.9,
    "return_citations": True,
    "search_domain_filter": ["perplexity.ai"],
    "return_images": False,
    "return_related_questions": False,
    "search_recency_filter": "month",
    "top_k": 0,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 1
}
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
