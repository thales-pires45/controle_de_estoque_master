from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from .models import Estoque_Itens_Saida, Estoque_Saida
from .forms import Estoque_Itens_Saida_Form, EstoqueForm


# Listar
from ..produto.models import Produto


class EstoqueSaidaList(ListView):
    model = Estoque_Saida
    template_name = 'estoque_saida_list.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Estoque_Saida.objects.filter(user=self.request.user)
        return self.object_list


# Update
class Estoque_Saida_Detail(DetailView):
    model = Estoque_Saida
    template_name = 'estoque_saida_detail.html'


# Inserir
def dar_baixa_estoque(form):
    # Pega os produtos a partir da instancia do formulario(Estoque).
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
        print('Estoque atualizado com sucesso.')


def estoque_saida_add(request):
    template_name = 'estoque_saida_item_form.html'
    estoque_form = Estoque_Saida()
    item_estoque_formset = inlineformset_factory(
        Estoque_Saida,
        Estoque_Itens_Saida,
        form=Estoque_Itens_Saida_Form,
        extra=0,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
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
            url = 'saida:estoque_saida_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


# Deletar
class deletarSaida(DeleteView):
    model = Estoque_Saida
    template_name = 'estoque_saida_confirm_delete.html'
    form_class = EstoqueForm


def confirm_deletar_Saida(request, pk):
    post = get_object_or_404(Estoque_Saida, pk=pk)
    post.delete()
    return redirect('saida:estoque_saida_list')
