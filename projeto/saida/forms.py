from django import forms
from .models import Estoque_Saida, Estoque_Itens_Saida
from projeto.produto.models import Produto


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque_Saida
        fields = ('nf',)


class Estoque_Itens_Saida_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Itens_Saida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Estoque_Itens_Saida_Form, self).__init__(*args, **kwargs)
        # Retorna somento produdos com estoque maior que zero
        self.fields['produto'].queryset = Produto.objects.filter(estoque__gt=0)
