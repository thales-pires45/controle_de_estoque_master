from django.db import models

from projeto.cliente.models import Cliente
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto


class Estoque_Saida(TimeStampedModel):
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} ... {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '...'


class Estoque_Itens_Saida(models.Model):
    estoque = models.ForeignKey(Estoque_Saida, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

        def __str__(self):
            return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
