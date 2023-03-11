from django import forms
from .models import Estoque_Saida, Estoque_Itens_Saida
from projeto.produto.models import Produto
from ..cliente.models import Cliente
from django.conf import settings

User = settings.AUTH_USER_MODEL


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque_Saida
        fields = ('nf', 'cliente',)

    def __init__(self, user, *args, **kwargs):
        super(EstoqueForm, self).__init__(*args, **kwargs)
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

# class EstoqueForm(forms.ModelForm):
#     class Meta:
#         model = Estoque_Saida
#         exclude = ['user']
#
#     def __init__(self, *args, **kwargs):
#         super(EstoqueForm, self).__init__(*args, **kwargs)
#         self.fields['cliente'].widget.attrs['autofocus'] = True
#
# class Estoque_Itens_Saida_Form(forms.ModelForm):
#     class Meta:
#         model = Estoque_Itens_Saida
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(Estoque_Itens_Saida_Form, self).__init__(*args, **kwargs)
#         self.fields['produto'].queryset = Produto.objects.filter(estoque__gt=0, user_id=kwargs['instance'].user.id)