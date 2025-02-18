**Aula: Integração do Celery em Projetos Django**  
---

### **Seção 1: Introdução ao Celery (15 minutos)**  
**Conteúdo:**  
1. **O que é o Celery?**  
   - Sistema de filas para processamento assíncrono.  
   - Casos de uso: envio de e-mails, processamento de dados, scraping, tarefas periódicas.  
   - Vantagens: melhorar performance, evitar bloqueio de requisições HTTP.  

2. **Componentes do Celery:**  
   - **Broker** (Redis/RabbitMQ): gerencia a fila de tarefas.  
   - **Worker**: processo que executa as tarefas.  
   - **Beat**: agendador de tarefas periódicas.  

3. **Fluxo de Funcionamento:**  
   - Django envia tarefas → Broker → Worker processa → Resultado armazenado (opcional).  

---

### **Seção 2: Configuração Inicial (25 minutos)**  
**Passo a Passo:**  
1. **Instalação:**  
   ```bash
   pip install celery[redis] django-celery-beat  # Instala Celery, Redis e o pacote para agendamento
   ```  

2. **Configuração do Broker (Redis):**  
   - Instale o Redis localmente ([guia de instalação](https://redis.io/docs/getting-started/)).  
   - Adicione ao `settings.py`:  
     ```python
     CELERY_BROKER_URL = 'redis://localhost:6379/0'
     CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
     CELERY_TIMEZONE = 'America/Sao_Paulo'
     ```  

3. **Criação do App Celery:**  
   - Arquivo `celery.py` (no diretório do projeto):  
     ```python
     import os
     from celery import Celery

     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto.settings')
     app = Celery('meu_projeto')
     app.config_from_object('django.conf:settings', namespace='CELERY')
     app.autodiscover_tasks()
     ```  
   - No `__init__.py` do projeto:  
     ```python
     from .celery import app as celery_app
     __all__ = ('celery_app',)
     ```  

**Demonstração Prática:**  
- Inicie o Redis:  
  ```bash
  redis-server
  ```  

---

### **Seção 3: Criando e Executando Tarefas (30 minutos)**  
**Conteúdo:**  
1. **Definindo Tarefas:**  
   - Crie um arquivo `tasks.py` em um app Django:  
     ```python
     from celery import shared_task

     @shared_task
     def processar_arquivo(nome_arquivo):
         # Simula processamento demorado
         import time
         time.sleep(10)
         return f"Arquivo {nome_arquivo} processado!"
     ```  

2. **Chamando Tarefas Assíncronas:**  
   - Em uma view ou serviço do Django:  
     ```python
     from .tasks import processar_arquivo

     def minha_view(request):
         processar_arquivo.delay("dados.csv")  # Envia para a fila
         return HttpResponse("Tarefa iniciada!")
     ```  

3. **Iniciando o Worker:**  
   ```bash
   celery -A meu_projeto worker --loglevel=info
   ```  

**Exercício Prático:**  
- Crie uma tarefa que simule o envio de um e-mail (apenas um `print`) e teste-a via Django Shell.  

---

### **Seção 4: Tarefas Periódicas com Celery Beat (20 minutos)**  
**Conteúdo:**  
1. **Configuração do Agendamento:**  
   - No `settings.py`:  
     ```python
     from celery.schedules import crontab

     CELERY_BEAT_SCHEDULE = {
         'limpar_cache_diario': {
             'task': 'meu_app.tasks.limpar_cache',
             'schedule': crontab(hour=0, minute=0),  # Meia-noite
         },
     }
     ```  

2. **Tarefa de Exemplo:**  
   ```python
   @shared_task
   def limpar_cache():
       from django.core.cache import cache
       cache.clear()
       return "Cache limpo!"
   ```  

3. **Iniciando o Celery Beat:**  
   ```bash
   celery -A meu_projeto beat --loglevel=info
   ```  

**Dica:** Use `django-celery-beat` para agendamentos dinâmicos via admin do Django.  

---

### **Seção 5: Boas Práticas e Solução de Problemas (10 minutos)**  
**Boas Práticas:**  
- Use filas separadas para prioridades diferentes (ex: `celery -A meu_projeto worker -Q alta_prioridade`).  
- Monitore com **Flower** (`pip install flower`, depois `celery -A meu_projeto flower`).  

**Problemas Comuns:**  
- **Redis não está rodando:** Verifique com `redis-cli ping`.  
- **Tarefas não descobertas:** Confira se `app.autodiscover_tasks()` está no `celery.py`.  
- **Fuso horário incorreto:** Defina `CELERY_TIMEZONE` e `TIME_ZONE` no Django.  

---

### **Encerramento e Exercício Final (10 minutos)**  
**Exercício:**  
1. Crie uma tarefa que gera um relatório em PDF (simule com um sleep).  
2. Agende-a para rodar a cada 5 minutos.  
3. Teste o fluxo completo (Django → Broker → Worker → Resultado).  

**Recursos Adicionais:**  
- [Documentação Oficial do Celery](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)  
- [Tutorial: Tarefas Assíncronas com Django e Celery (Real Python)](https://realpython.com/asynchronous-tasks-with-django-and-celery/)  

**Q&A:**  
- "Como usar RabbitMQ em vez do Redis?"  
- "Como debugar tarefas falhas?"  
- "Como escalar workers em produção?"  

--- 

**Pronto!** Com esta aula, os alunos poderão integrar o Celery em projetos Django para tarefas assíncronas e agendadas, melhorando a eficiência de suas aplicações.