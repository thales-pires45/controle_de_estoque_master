from django import forms

from projeto.produto.models import Produto
from .models import Estoque_Saida, Estoque_Itens_Saida
from ..cliente.models import Cliente


class Estoque_Saida_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Saida
        fields = ('nf', 'cliente',)

    def __init__(self, user, *args, **kwargs):
        super(Estoque_Saida_Form, self).__init__(*args, **kwargs)
        # Retorna somento produdos com estoque maior que zero
        self.fields['cliente'].queryset = Cliente.objects.filter(user_id=user.id)


class Estoque_Itens_Saida_Form(forms.ModelForm):
    class Meta:
        model = Estoque_Itens_Saida
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(Estoque_Itens_Saida_Form, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['produto'].queryset = Produto.objects.filter(estoque__gt=0, user_id=user.id)


