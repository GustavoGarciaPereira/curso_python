from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=220)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.preco} - {self.estoque} - {self.descricao}"
