from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from cliente.models import Cliente
from produto.models import Produto
from saida.models import Estoque_Itens_Saida, Estoque_Saida
from entrada.models import Estoque_Itens_Entrada, Estoque_Entrada


@login_required(login_url='/auth/login')
def index(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        return redirect('usuario:login')


def retorna_total_vendido(request):
    if request.user.is_authenticated:
        venda_user = Estoque_Itens_Saida.objects.filter(estoque__user=request.user)
        total = venda_user.aggregate(Sum('valor_total'))['valor_total__sum']
        if total is None:
            total = 0
        return JsonResponse({'total': total})
    else:
        return JsonResponse({'error': 'Usuário não autenticado.'})


def relatorio_faturamento(request):
    if request.user.is_authenticated:
        venda_user = Estoque_Itens_Saida.objects.filter(estoque__user=request.user)
        x = venda_user.aggregate(Sum('valor_total'))['valor_total__sum']

        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        data = []
        labels = []

        today = datetime.now()
        for i in range(12):
            start_date = today - timedelta(days=30)
            end_date = today

            y = venda_user.filter(data__gte=start_date, data__lt=end_date).aggregate(Sum('valor_total'))[
                'valor_total__sum']
            if y is None:
                y = 0
            labels.append(meses[today.month - 1])
            data.append(y)

            today = start_date
        data_json = {'data': data[::-1], 'labels': labels[::-1]}
        return JsonResponse(data_json)
    else:
        return JsonResponse({'error': 'Usuário não autenticado.'})


def relatorio_produtos(request):
    produtos = Produto.objects.filter(user=request.user)
    labels = []
    data = []

    for produto in produtos:
        venda_user = Estoque_Itens_Saida.objects.filter(estoque__user=request.user)
        vendas = venda_user.filter(produto=produto).aggregate(Sum('valor_total'))
        valor_total = vendas['valor_total__sum'] or 0
        labels.append(produto.produto)
        data.append(valor_total)

    zipped_data = list(zip(labels, data))
    # Sort ordena de maior para menor
    zipped_data.sort(key=lambda x: x[1], reverse=True)
    # Divide a Dupla
    labels, data = zip(*zipped_data)
    # Retorna os 5 mais vendidos
    return JsonResponse({'labels': labels[:5], 'data': data[:5]})


def retorna_total_comprado(request):
    if request.user.is_authenticated:
        entrada_user = Estoque_Itens_Entrada.objects.filter(estoque__user=request.user)
        total = entrada_user.aggregate(Sum('valor_total'))['valor_total__sum']
        if total is None:
            total = 0
        return JsonResponse({'total': total})
    else:
        return JsonResponse({'error': 'Usuário não autenticado.'})


def relatorio_entrada(request):
    if request.user.is_authenticated:
        entrada_user = Estoque_Itens_Entrada.objects.filter(estoque__user=request.user)
        x = entrada_user.aggregate(Sum('valor_total'))['valor_total__sum']

        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        data = []
        labels = []

        today = datetime.now()
        for i in range(12):
            start_date = today - timedelta(days=30)
            end_date = today

            y = entrada_user.filter(data__gte=start_date, data__lt=end_date).aggregate(Sum('valor_total'))[
                'valor_total__sum']
            if y is None:
                y = 0
            labels.append(meses[today.month - 1])
            data.append(y)

            today = start_date
        data_json = {'data': data[::-1], 'labels': labels[::-1]}
        return JsonResponse(data_json)
    else:
        return JsonResponse({'error': 'Usuário não autenticado.'})


def relatorio_produtos_entrada(request):
    produtos = Produto.objects.filter(user=request.user)
    labels = []
    data = []

    for produto in produtos:
        entrada_user = Estoque_Itens_Entrada.objects.filter(estoque__user=request.user)
        vendas = entrada_user.filter(produto=produto).aggregate(Sum('valor_total'))
        valor_total = vendas['valor_total__sum'] or 0
        labels.append(produto.produto)
        data.append(valor_total)

    zipped_data = list(zip(labels, data))
    # Sort ordena de maior para menor
    zipped_data.sort(key=lambda x: x[1], reverse=True)
    # Divide a Dupla
    labels, data = zip(*zipped_data)
    # Retorna os 5 mais vendidos
    return JsonResponse({'labels': labels[:5], 'data': data[:5]})


def retorna_diferenca_comprado_vendido(request):
    if request.user.is_authenticated:
        entrada_user = Estoque_Itens_Entrada.objects.filter(estoque__user=request.user)
        total_comprado = entrada_user.aggregate(Sum('valor_total'))['valor_total__sum']
        if total_comprado is None:
            total_comprado = 0

        venda_user = Estoque_Itens_Saida.objects.filter(estoque__user=request.user)
        total_vendido = venda_user.aggregate(Sum('valor_total'))['valor_total__sum']
        if total_vendido is None:
            total_vendido = 0

        diferenca = total_vendido - total_comprado

        return JsonResponse({'total': diferenca})
    else:
        return JsonResponse({'error': 'Usuário não autenticado.'})
