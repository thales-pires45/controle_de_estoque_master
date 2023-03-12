from django.conf import settings
from django.db import models
from django.urls import reverse_lazy

User = settings.AUTH_USER_MODEL


class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque minimo', default=0)
    data = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    # acessar o produto
    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})

    # Buscar o Produto Id e Estoque
    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }
