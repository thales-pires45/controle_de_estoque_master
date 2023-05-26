from django.urls import path

from saida import views

app_name = 'saida'

urlpatterns = [
    path('<int:pk>/', views.Estoque_Saida_Detail.as_view(), name='estoque_saida_detail'),
    path('', views.EstoqueSaidaList.as_view(), name='estoque_saida_list'),
    path('add/', views.estoque_saida_add, name='estoque_saida_add'),
    path('deletar/estoque/saida/<int:pk>/', views.deletarSaida.as_view(), name='estoque_saida_delete'),
    path('deletar/cofirmado/estoque/saida/<int:pk>', views.confirm_deletar_Saida, name='confirm_estoque_saida_delete')

]
