from django.urls import path
from cliente import views

app_name = 'cliente'

urlpatterns = [
    path('', views.listaCliente.as_view(), name='cliente_list'),
    path('<int:pk>/', views.detailCliente, name='cliente_detail'),
    path('add/cliente', views.cadastroCliente.as_view(), name='cliente_add'),
    path('edit/cliente/<int:pk>', views.editCliente.as_view(), name='cliente_edit'),
    path('deletar/cliente/<int:pk>/', views.deletarCliente.as_view(), name='cliente_delete'),
    path('deletar/cofirmado/cliente/<int:pk>', views.confirm_deletar_Cliente, name='confirm_cliente_delete')
]
