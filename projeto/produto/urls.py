from django.urls import path
from projeto.produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.listaProduto.as_view(), name='produto_list'),
    path('<int:pk>/', v.detailProduto, name='produto_detail'),
    path('add', v.cadastroProduto.as_view(), name='produto_add'),
    path('edit/<int:pk>', v.editProduto.as_view(), name='produto_edit'),
    path('deletar/<int:pk>/', v.deletarProduto.as_view(), name='produto_delete'),
    path('delet/<int:pk>', v.confirm_deletar_Produto, name='confirm_produto_delete'),
    path('<int:pk>/json/', v.produto_json, name='produto_json'),
]
