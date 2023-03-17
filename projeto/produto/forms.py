from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto', 'preco', 'estoque', 'estoque_minimo']
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'preco': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'estoque': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'estoque_minimo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }
