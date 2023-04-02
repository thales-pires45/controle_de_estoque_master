import re
from django import forms
from django.core import validators
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente', 'telefone', 'rua', 'numero', 'cep']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        telefone = cleaned_data.get('telefone')
        cep = cleaned_data.get('cep')

        if telefone:
            telefone = re.sub('[^0-9]', '', telefone)
            if len(telefone) == 11:
                cleaned_data['telefone'] = '({}){} {}-{}'.format(telefone[:2], telefone[2:3], telefone[3:7],
                                                                 telefone[7:])
            elif len(telefone) == 10:
                cleaned_data['telefone'] = '({}){} {}-{}'.format(telefone[:2], telefone[2], telefone[3:6], telefone[6:])
            else:
                raise forms.ValidationError('Telefone inválido. Deve conter 11 dígitos.')

        if cep:
            cep = re.sub('[^0-9]', '', cep)
            if len(cep) == 8:
                cleaned_data['cep'] = '{}-{}'.format(cep[:5], cep[5:])
            else:
                raise forms.ValidationError('CEP inválido.')

        return cleaned_data
