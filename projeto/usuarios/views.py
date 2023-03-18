from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect


def login(request):
    if request.user.is_authenticated:
        return redirect('/core/home/')
    else:
        status = request.GET.get('status')
        return render(request, 'login.html', {'status': status})


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/core/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):

    nome = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    senha2 = request.POST.get('password2')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Email ou senha não podem ficar vazio')
        return redirect('/auth/cadastro/')

    if senha != senha2:
        messages.add_message(request, constants.ERROR, 'Suas senhas não são as mesmas')
        return redirect('/auth/cadastro/')

    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no mínimo 8 caracteres')
        return redirect('/auth/cadastro/')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse email')
        return redirect('/auth/cadastro/')

    if User.objects.filter(username=nome).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome')
        return redirect('/auth/cadastro/')

    try:

        usuario = User.objects.create_user(username=nome, email=email, password=senha)
        usuario.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')

        user = authenticate(request, username=nome, password=senha)
        auth.login(request, user)
        return redirect('/core/home/')

    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/auth/cadastro/')


def valida_login(request):
    username_or_email = request.POST.get('username_or_email')
    senha = request.POST.get('senha')

    usuario = authenticate(request, username=username_or_email, password=senha)
    if not usuario:
        messages.add_message(request, constants.WARNING, 'usuário ou senha inválido')
        return redirect('/auth/login/')
    else:
        auth.login(request, usuario)
        return redirect('/core/home/')


def sair(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING, 'Faça login antes de acessar a plataforma')
    return redirect('/auth/login/')
