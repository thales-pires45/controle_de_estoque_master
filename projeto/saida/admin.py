from django.contrib import admin

from .models import Estoque_Saida, Estoque_Itens_Saida


class EstoqueItensInline(admin.TabularInline):
    model = Estoque_Itens_Saida
    extra = 0


@admin.register(Estoque_Saida)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf',)
    search_fields = ('nf',)
    date_hierarchy = 'created'
