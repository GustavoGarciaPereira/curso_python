from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=220)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)
    tags = models.JSONField(default=list, blank=True)  # Novo campo para armazenar as tags


    def __str__(self):
        return f"{self.nome} - R${self.preco} - {self.estoque}"
