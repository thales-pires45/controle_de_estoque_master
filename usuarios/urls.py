from django.urls import path
from django.contrib.auth.decorators import login_required
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('valida_login/', views.valida_login, name='valida_login'),
    path('sair/', views.sair, name='sair'),
    path('atualizar-cadastro/', login_required(views.atualizar_cadastro), name='atualizar_cadastro'),
    path('redefinir-senha/', login_required(views.redefinir_senha), name='password_reset'),
    path('esqueci-senha-login/', views.redefinir_senha_login, name='esqueceu_senha_login'),
    # path('esqueci-senha/', views.esqueceu_senha, name='esqueceu_senha'),

]
