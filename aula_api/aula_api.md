### **Aula: Integração com APIs em Python**

#### **1. Introdução a APIs**
- **O que é uma API?**  
  Uma _Interface de Programação de Aplicações_ (API) permite que sistemas se comuniquem. Exemplo: enviar uma solicitação a um servidor e receber uma resposta.

- **Conceitos-chave**:  
  - **Endpoint**: URL da API (ex: `https://api.openai.com/v1/chat/completions`).  
  - **Métodos HTTP**: GET (ler dados), POST (enviar dados), PUT/PATCH (atualizar), DELETE.  
  - **Autenticação**: Chaves de API (ex: `Bearer TOKEN`).  
  - **Formato de dados**: JSON (comum em APIs modernas).

---

#### **2. Exemplo Prático: Integração com OpenAI API**
Vamos usar a biblioteca `requests` do Python para enviar uma solicitação à API da OpenAI (simulando o que seria feito com a Perplexity, se disponível).

##### **Passo 1: Instalação**
```bash
pip install requests python-dotenv
```

##### **Passo 2: Configuração**
1. Crie uma conta em [OpenAI](https://platform.openai.com/) e gere uma chave de API.  
2. Crie um arquivo `.env` para armazenar a chave:
   ```ini
   OPENAI_API_KEY=sua_chave_aqui
   ```
3. Crie um arquivo `app.py`.

##### **Passo 3: Código Python**
```python
import os
import requests
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
URL = "https://api.openai.com/v1/chat/completions"

# Configuração do cabeçalho e corpo da requisição
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Explique o que é uma API em 1 frase."}
    ]
}

# Envia a requisição POST
response = requests.post(URL, headers=headers, json=data)

# Processa a resposta
if response.status_code == 200:
    resposta = response.json()
    print(resposta['choices'][0]['message']['content'])
else:
    print(f"Erro: {response.status_code} - {response.text}")
```

##### **Passo 4: Execução**
```bash
python app.py
```

**Saída Esperada**:  
```
Uma API é uma interface que permite que diferentes sistemas ou componentes de software se comuniquem e compartilhem dados.
```

---

#### **3. Adaptação para Outras APIs**
Se preferir usar outra API (como a do Google, Twitter, ou uma API fictícia), siga estes passos:  
1. **Documentação da API**: Busque o endpoint, método HTTP e formato de dados exigido.  
2. **Autenticação**: Configure tokens ou chaves necessárias.  
3. **Teste**: Use ferramentas como [Postman](https://www.postman.com/) ou `curl` para validar antes de codificar.

---

#### **4. Boas Práticas**
- **Segurança**: Nunca exponha chaves de API publicamente (use `.env` ou variáveis de ambiente).  
- **Tratamento de Erros**: Sempre verifique `response.status_code`.  
- **Limites de Uso**: Respeite os rate limits da API.

---

### **Observação sobre a Perplexity**
Se a Perplexity lançar uma API no futuro, substitua a URL e os parâmetros no código conforme a documentação oficial. APIs de modelos de linguagem geralmente seguem padrões similares (como no exemplo da OpenAI).