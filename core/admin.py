from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.db.models import Count
from django.template.response import TemplateResponse
from .models import Categoria, Localizacao, Item

admin.site.unregister(Group)

# ── Inline ──────────────────────────────────────────────────────────────────
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


# ── Dashboard no index do admin ──────────────────────────────────────────────
original_index = admin.site.__class__.index

def custom_index(self, request, extra_context=None):
    total_itens       = Item.objects.count()
    total_perdidos    = Item.objects.filter(tipo='perdido').count()
    total_encontrados = Item.objects.filter(tipo='encontrado').count()
    total_abertos     = Item.objects.filter(status='aberto').count()
    total_resolvidos  = Item.objects.filter(status='resolvido').count()
    total_usuarios    = User.objects.count()

    pct_resolvidos = round(total_resolvidos / total_itens * 100) if total_itens else 0
    pct_perdidos   = round(total_perdidos   / total_itens * 100) if total_itens else 0

    top_categorias = (
        Categoria.objects
        .annotate(total=Count('item'))
        .filter(total__gt=0)
        .order_by('-total')[:5]
    )
    top_localizacoes = (
        Localizacao.objects
        .annotate(total=Count('item'))
        .filter(total__gt=0)
        .order_by('-total')[:5]
    )

    extra_context = extra_context or {}
    extra_context.update({
        'total_itens': total_itens,
        'total_perdidos': total_perdidos,
        'total_encontrados': total_encontrados,
        'total_abertos': total_abertos,
        'total_resolvidos': total_resolvidos,
        'total_usuarios': total_usuarios,
        'pct_resolvidos': pct_resolvidos,
        'pct_perdidos': pct_perdidos,
        'top_categorias': top_categorias,
        'top_localizacoes': top_localizacoes,
    })
    return original_index(self, request, extra_context)

admin.site.__class__.index = custom_index
