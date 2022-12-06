from django.urls import include, path
from projeto.relatorio import views

app_name = 'relatorio'

urlpatterns = [
    path('produto/', views.RelatorioProduto.as_view(), name='relatorio_produto'),
    path('cliente/', views.RelatorioCliente.as_view(), name='relatorio_cliente'),
    path('entrada/', views.RelatorioEntrada.as_view(), name='relatorio_entrada'),
    path('saida/', views.RelatorioSaida.as_view(), name='relatorio_saida'),
]