from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('retorna_total_vendido/', views.retorna_total_vendido, name='retorna_total_vendido'),
    path('relatorio_faturamento/', views.relatorio_faturamento, name='relatorio_faturamento'),
    path('relatorio_produtos/', views.relatorio_produtos, name='relatorio_produtos'),
]