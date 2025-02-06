Vou implementar o **Sistema de Votação (Enquetes)** passo a passo. Vamos criar uma aplicação chamada `enquetes`:

---

### **1. Configuração Inicial**  
```bash
python manage.py startapp enquetes
```

Registre a app em `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'enquetes',
]
```

---

### **2. Modelos (`models.py`)**  
```python
from django.db import models
from django.utils import timezone

class Enquete(models.Model):
    pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pergunta

class Opcao(models.Model):
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE, related_name='opcoes')
    texto_opcao = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcao
```

Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **3. Admin (`admin.py`)**  
```python
from django.contrib import admin
from .models import Enquete, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 3  # 3 opções por padrão

@admin.register(Enquete)
class EnqueteAdmin(admin.ModelAdmin):
    inlines = [OpcaoInline]
    list_display = ['pergunta', 'data_publicacao']

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ['texto_opcao', 'votos']
```

---

### **4. Views (`views.py`)**  
```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Enquete, Opcao

def lista_enquetes(request):
    enquetes = Enquete.objects.all()
    return render(request, 'enquetes/lista.html', {'enquetes': enquetes})

def detalhes_enquete(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render(request, 'enquetes/votar.html', {'enquete': enquete})

def votar(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    try:
        opcao_selecionada = enquete.opcoes.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'enquetes/votar.html', {
            'enquete': enquete,
            'error_message': "Selecione uma opção válida."
        })
    else:
        opcao_selecionada.votos += 1
        opcao_selecionada.save()
        return redirect('resultados', enquete_id=enquete.id)

def resultados(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render(request, 'enquetes/resultados.html', {'enquete': enquete})
```

---

### **5. URLs (`urls.py` no app `enquetes`)**  
```python
from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.lista_enquetes, name='lista'),
    path('<int:enquete_id>/', views.detalhes_enquete, name='detalhes'),
    path('<int:enquete_id>/votar/', views.votar, name='votar'),
    path('<int:enquete_id>/resultados/', views.resultados, name='resultados'),
]
```

Inclua no `urls.py` do projeto:
```python
from django.urls import include, path

urlpatterns = [
    ...
    path('enquetes/', include('enquetes.urls')),
]
```

---

### **6. Templates**  

#### `enquetes/templates/enquetes/lista.html` (Lista de Enquetes):
```html
<h1>Enquetes Disponíveis</h1>
<ul>
    {% for enquete in enquetes %}
        <li>
            <a href="{% url 'enquetes:detalhes' enquete.id %}">{{ enquete.pergunta }}</a>
        </li>
    {% endfor %}
</ul>
```

#### `enquetes/templates/enquetes/votar.html` (Página de Votação):
```html
<h1>{{ enquete.pergunta }}</h1>
<form method="post" action="{% url 'enquetes:votar' enquete.id %}">
    {% csrf_token %}
    {% for opcao in enquete.opcoes.all %}
        <input type="radio" name="opcao" id="opcao{{ forloop.counter }}" value="{{ opcao.id }}">
        <label for="opcao{{ forloop.counter }}">{{ opcao.texto_opcao }}</label><br>
    {% endfor %}
    <input type="submit" value="Votar">
</form>
{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
```

#### `enquetes/templates/enquetes/resultados.html` (Resultados com Gráfico):
```html
<h1>Resultados: {{ enquete.pergunta }}</h1>
<ul>
    {% for opcao in enquete.opcoes.all %}
        <li>{{ opcao.texto_opcao }}: {{ opcao.votos }} voto{{ opcao.votos|pluralize }}</li>
    {% endfor %}
</ul>

<!-- Gráfico com Chart.js -->
<canvas id="graficoResultados" width="400" height="200"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const ctx = document.getElementById('graficoResultados').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [{% for opcao in enquete.opcoes.all %}'{{ opcao.texto_opcao }}',{% endfor %}],
            datasets: [{
                label: 'Votos',
                data: [{% for opcao in enquete.opcoes.all %}{{ opcao.votos }},{% endfor %}],
                backgroundColor: 'rgba(54, 162, 235, 0.5)',
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>

<a href="{% url 'enquetes:lista' %}">Voltar para a lista</a>
```

---

### **7. Testando**  
1. Acesse o admin (`/admin`) e crie uma enquete com opções.  
2. Acesse `http://localhost:8000/enquetes/` para ver a lista.  
3. Clique em uma enquete para votar.  
4. Após votar, você será redirecionado para a página de resultados com o gráfico.

---

### **Melhorias Sugeridas**  
1. **Autenticação:** Restringir votos a usuários logados.  
2. **Cookie/Sessão:** Evitar votos duplicados.  
3. **Estilização:** Adicionar CSS para melhorar a aparência.  
4. **Ordenação:** Mostrar opções por número de votos.  