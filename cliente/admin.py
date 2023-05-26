from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cliente',
        'telefone',
        'cep',
        'rua',
        'numero',
        'data_cliente',
    )
    search_fields = ('cliente',)
