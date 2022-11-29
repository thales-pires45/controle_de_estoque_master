from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Produto
from .forms import ProdutoForm
from django.http import JsonResponse


# LISTAR
class listaProduto(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produto_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(listaProduto, self).get_queryset()
        return queryset


# INSERIR
class cadastroProduto(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


# EDITAR
class editProduto(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


def detailProduto(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


# Deletar
class deletarProduto(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    form_class = ProdutoForm


def confirm_deletar_Produto(request, pk):
    post = get_object_or_404(Produto, pk=pk)
    post.delete()
    return redirect('produto:produto_list')


# Retorna o Produto Id e Estoque
def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
