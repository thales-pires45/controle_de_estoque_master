from django.views.generic import ListView

from projeto.entrada.models import Estoque_Entrada
from projeto.produto.models import Produto
from projeto.cliente.models import Cliente


# Listar Produto
from projeto.saida.models import Estoque_Saida


class RelatorioProduto(ListView):
    model = Produto
    template_name = 'relatorio_produto.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(RelatorioProduto, self).get_queryset()
        return queryset


# Listar Cliente
class RelatorioCliente(ListView):
    model = Cliente
    template_name = 'relatorio_cliente.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(RelatorioCliente, self).get_queryset()
        return queryset


# Listar Entrada
class RelatorioEntrada(ListView):
    model = Estoque_Entrada
    template_name = 'relatorio_entrada.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(RelatorioEntrada, self).get_queryset()
        return queryset


# Listar Entrada
class RelatorioSaida(ListView):
    model = Estoque_Saida
    template_name = 'relatorio_saida.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(RelatorioSaida, self).get_queryset()
        return queryset
