from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Categoria, Localizacao, Item

admin.site.unregister(Group)

class ItemInline(admin.TabularInline):
    model = Item
    fields = ('titulo', 'tipo', 'status', 'localizacao', 'categoria')
    readonly_fields = ('titulo', 'tipo', 'status', 'localizacao', 'categoria')
    extra = 0
    can_delete = False

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    inlines = [ItemInline]

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'status', 'categoria', 'localizacao', 'autor', 'data')
    list_filter = ('tipo', 'status', 'categoria')
    search_fields = ('titulo', 'descricao')
