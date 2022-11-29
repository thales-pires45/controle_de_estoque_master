from django.contrib import admin
from .models import Estoque_Entrada, Estoque_Itens_Entrada


class EstoqueItensInline(admin.TabularInline):
    model = Estoque_Itens_Entrada
    extra = 0


@admin.register(Estoque_Entrada)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf',)
    search_fields = ('nf',)
    date_hierarchy = 'created'