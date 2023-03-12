from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from .forms import ClienteForm
from .models import Cliente


# LISTAR
class listaCliente(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Cliente.objects.filter(user=self.request.user)
        return self.object_list


# INSERIR
class cadastroCliente(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['cliente', 'telefone', 'cep', 'rua', 'numero']

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url


# EDITAR
class editCliente(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm


def detailCliente(request, pk):
    template_name = 'cliente_detail.html'
    obj = Cliente.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


# Deletar
class deletarCliente(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    form_class = ClienteForm


def confirm_deletar_Cliente(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    post.delete()
    return redirect('cliente:cliente_list')
