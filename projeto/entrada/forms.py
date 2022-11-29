from projeto.entrada.models import Estoque_Itens_Entrada, Estoque_Entrada
from django import forms


class Estoque_Entrada_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Entrada
        fields = ('nf',)


class Estoque_Itens_Entrada_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Itens_Entrada
        fields = '__all__'
