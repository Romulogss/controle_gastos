"""
Framework Django, utilizando módulo db para fazer conexão com o Banco de Dados
"""
from django.db import models


# Create your models here.

class Categoria(models.Model):
    """
    Tabela categoria
    """
    nome = models.CharField(max_length=100)
    dt_resgitrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        converter objeto em um string
        :return: atributo nome como uma string
        """
        return self.nome


class Transacao(models.Model):
    """
    Tabela Transação
    """
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        converter objeto em um string
        :return: atributo descricao como uma string
        """
        return self.descricao

    class Meta:
        """
        Meta class
        """
        verbose_name_plural = "Transações"
