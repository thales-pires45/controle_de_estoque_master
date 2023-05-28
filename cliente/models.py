from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse_lazy
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Cliente(models.Model):
    cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    cep = models.CharField('cep', max_length=9, blank=True)
    rua = models.CharField('rua', max_length=100, blank=True)
    numero = models.IntegerField('numero', blank=True, null=True)
    data_cliente = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ('cliente',)
        constraints = [
            UniqueConstraint(fields=['user', 'cliente'], name='unique_user_cliente'),
        ]

    def __str__(self):
        return self.cliente

    def get_absolute_url(self):
        return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})
