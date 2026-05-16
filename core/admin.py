from django.contrib import admin
from .models import Categoria, Localizacao, Item

admin.site.site_header = 'Achados e Perdidos — UFLA'
admin.site.site_title = 'Achados e Perdidos'
admin.site.index_title = 'Painel Administrativo'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'status', 'categoria', 'localizacao', 'autor', 'data')
    list_filter = ('tipo', 'status', 'categoria')
    search_fields = ('titulo',)
