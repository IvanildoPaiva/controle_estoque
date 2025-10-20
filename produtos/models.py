from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.nome