from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente', 'telefone', 'rua', 'numero', 'cep']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def clean_telefone(self):
    #     telefone = self.cleaned_data['telefone']
    #     if not telefone.isnumeric():
    #         raise forms.ValidationError('O telefone deve conter apenas números.')
    #     return telefone
    #
    # def clean_cep(self):
    #     telefone = self.cleaned_data['cep']
    #     if not telefone.isnumeric():
    #         raise forms.ValidationError('O cep deve conter apenas números.')
    #     return telefone
