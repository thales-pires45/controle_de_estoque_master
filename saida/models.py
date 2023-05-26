from django.conf import settings
from django.db import models

from cliente.models import Cliente
from core.models import TimeStampedModel
from produto.models import Produto

User = settings.AUTH_USER_MODEL


class Estoque_Saida(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

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
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)
    valor_total = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

        def __str__(self):
            return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
