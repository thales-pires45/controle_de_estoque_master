from django.db import models
from django.urls import reverse_lazy
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Cliente(models.Model):
    cliente = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=24)
    cep = models.CharField('cep', max_length=8, blank=True)
    rua = models.CharField('rua', max_length=100, blank=True)
    numero = models.IntegerField('numero', blank=True, null=True)
    data_cliente = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ('cliente',)

    def __str__(self):
        return self.cliente

    # acessar cliente
    def get_absolute_url(self):
        return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})
