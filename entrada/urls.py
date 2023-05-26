from django.urls import path

from entrada import views

app_name = 'entrada'

urlpatterns = [
    path('<int:pk>/', views.Estoque_Entrada_Detail.as_view(), name='estoque_entrada_detail'),
    path('', views.EstoqueEntradaList.as_view(), name='estoque_entrada_list'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),
    path('deletar/estoque/entrada/<int:pk>/', views.deletarEntrada.as_view(), name='estoque_entrada_delete'),
    path('deletar/cofirmado/estoque/entrada/<int:pk>', views.confirm_deletar_Entrada,
         name='confirm_estoque_entrada_delete'),

]
