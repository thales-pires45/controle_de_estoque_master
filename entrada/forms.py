from django import forms

from entrada.models import Estoque_Itens_Entrada, Estoque_Entrada
from produto.models import Produto


class Estoque_Entrada_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Entrada
        fields = ('nf',)


class Estoque_Itens_Entrada_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Itens_Entrada
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(Estoque_Itens_Entrada_Form, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['produto'].queryset = Produto.objects.filter(user_id=user.id)
