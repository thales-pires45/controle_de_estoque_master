from django.views.generic import ListView

from projeto.cliente.models import Cliente
from projeto.entrada.models import Estoque_Entrada
from projeto.produto.models import Produto
from projeto.saida.models import Estoque_Saida


# Listar Produto
class RelatorioProduto(ListView):
    model = Produto
    template_name = 'relatorio_produto.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Produto.objects.filter(user=self.request.user)
        return self.object_list


# Listar Cliente
class RelatorioCliente(ListView):
    model = Cliente
    template_name = 'relatorio_cliente.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Cliente.objects.filter(user=self.request.user)
        return self.object_list


# Listar Entrada
class RelatorioEntrada(ListView):
    model = Estoque_Entrada
    template_name = 'relatorio_entrada.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Estoque_Entrada.objects.filter(user=self.request.user)
        return self.object_list


# Listar Entrada
class RelatorioSaida(ListView):
    model = Estoque_Saida
    template_name = 'relatorio_saida.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Estoque_Saida.objects.filter(user=self.request.user)
        return self.object_list
