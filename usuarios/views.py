from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
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


@login_required
def atualizar_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        email = request.POST.get('email')

        user = request.user

        try:
            existing_user = User.objects.get(username=nome)
            existing_email = User.objects.get(email=email)
            if existing_user != user:
                messages.error(request, 'O nome de usuário já está em uso.')
                return redirect('usuarios:atualizar_cadastro')

            if existing_email != user:
                messages.error(request, 'O email de usuário já está em uso.')
                return redirect('usuarios:atualizar_cadastro')

        except User.DoesNotExist:
            pass

        user.username = nome
        user.email = email
        user.save()

        messages.success(request, 'Cadastro atualizado com sucesso!')
        return redirect('/auth/atualizar-cadastro/')

    else:
        return render(request, 'atualizar_cadastro.html')


@login_required
def redefinir_senha(request):
    if request.method == 'POST':
        senha_atual = request.POST.get('senha_atual')
        nova_senha = request.POST.get('nova_senha')
        confirmar_nova_senha = request.POST.get('confirmar_nova_senha')

        if not request.user.check_password(senha_atual):
            messages.error(request, 'A senha atual está incorreta.')
            return redirect('usuarios:password_reset')

        if nova_senha != confirmar_nova_senha:
            messages.error(request, 'A nova senha e a confirmação da nova senha não são iguais.')
            return redirect('usuarios:password_reset')

        if len(nova_senha) < 8:
            messages.error(request, 'A nova senha deve ter pelo menos 8 caracteres.')
            return redirect('usuarios:password_reset')

        request.user.set_password(nova_senha)
        request.user.save()

        messages.success(request, 'Sua senha foi atualizada com sucesso!')

        user = authenticate(request, username=request.user, password=nova_senha)
        auth.login(request, user)
        return redirect('usuarios:password_reset')

    else:
        return render(request, 'redefinir_senha.html')


def redefinir_senha_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nova_senha = request.POST.get('nova_senha')
        confirmar_nova_senha = request.POST.get('confirmar_nova_senha')

        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Não existe uma conta associada com esse email.')
            return redirect('usuarios:esqueceu_senha_login')

        if nova_senha != confirmar_nova_senha:
            messages.error(request, 'A nova senha e a confirmação da nova senha não são iguais.')
            return redirect('usuarios:esqueceu_senha_login')

        if len(nova_senha) < 8:
            messages.error(request, 'A nova senha deve ter pelo menos 8 caracteres.')
            return redirect('usuarios:esqueceu_senha_login')
        user = User.objects.get(email=email)

        user.set_password(nova_senha)
        user.save()

        messages.success(request, 'Sua senha foi atualizada com sucesso!')

        return redirect('usuarios:login')

    else:
        return render(request, 'esqueceu_senha_login.html')

# def esqueceu_senha(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#
#         if not User.objects.filter(email=email).exists():
#             messages.error(request, 'Não existe uma conta associada com esse email.')
#             return redirect('usuarios:esqueceu_senha')
#
#         user = User.objects.get(email=email)
#         token = default_token_generator.make_token(user)
#
#         reset_url = request.\
#             build_absolute_uri(reverse('usuarios:password_reset_confirm',
#                     kwargs={
#                         'uidb64': urlsafe_base64_encode(
#                             force_bytes(user.pk)),
#                             'token': token
#                     }))
#
#         # Aqui você pode enviar o link para o email do usuário usando uma biblioteca de envio de email, como o Django
#         # Sendgrid
#
#         messages.success(request, 'Enviamos um link de redefinição de senha para o seu email.')
#         return redirect('usuarios:login')
#
#     else:
#         return render(request, 'esqueceu_senha.html')
