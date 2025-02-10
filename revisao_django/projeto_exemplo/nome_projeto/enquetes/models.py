from django.db import models

# Create your models here.
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