from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from .forms import ProdutoForm
from .models import Produto


# LISTAR
class listaProduto(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'

    paginate_by = 10

    def get_queryset(self):
        self.object_list = Produto.objects.filter(user=self.request.user)
        return self.object_list


# INSERIR
class cadastroProduto(CreateView):
    model = Produto
    fields = ['produto', 'preco', 'estoque', 'estoque_minimo']
    template_name = 'produto_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)

        return url


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
