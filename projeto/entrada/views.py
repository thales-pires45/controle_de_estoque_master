from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.forms import inlineformset_factory
from projeto.produto.models import Produto
from django.http import HttpResponseRedirect
from .models import Estoque_Entrada, Estoque_Itens_Entrada
from .forms import Estoque_Entrada_Form, Estoque_Itens_Entrada_Form

# Listar
from ..saida.models import Estoque_Saida


# Listar
class EstoqueEntradaList(ListView):
    model = Estoque_Entrada
    template_name = 'estoque_entrada_list.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Estoque_Entrada.objects.filter(user=self.request.user)
        return self.object_list


# Update
class Estoque_Entrada_Detail(DetailView):
    model = Estoque_Entrada
    template_name = 'estoque_entrada_detail.html'


# Inserir
def dar_baixa_estoque(form):
    # Pega os produtos a partir da instancia do formulario(Estoque).
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
        print('Estoque atualizado com sucesso.')


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_item_form.html'
    estoque_form = Estoque_Entrada()
    item_estoque_formset = inlineformset_factory(
        Estoque_Entrada,
        Estoque_Itens_Entrada,
        form=Estoque_Itens_Entrada_Form,
        extra=0,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )

    if request.method == 'POST':
        form = Estoque_Entrada_Form(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form.instance.user = request.user
            form = form.save(commit=False)
            form.save()
            formset.save()
            dar_baixa_estoque(form)
            url = 'entrada:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = Estoque_Entrada_Form(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    context = {'form': form, 'formset': formset}

    return render(request, template_name, context)


# Deletar
class deletarEntrada(DeleteView):
    model = Estoque_Entrada
    template_name = 'estoque_entrada_confirm_delete.html'
    form_class = Estoque_Entrada_Form


def confirm_deletar_Entrada(request, pk):
    post = get_object_or_404(Estoque_Entrada, pk=pk)
    post.delete()
    return redirect('entrada:estoque_entrada_list')
