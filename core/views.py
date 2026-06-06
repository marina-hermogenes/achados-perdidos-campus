from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Item, Categoria, Localizacao


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def home(request):
    return render(request, 'home.html')


def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})


@login_required
def lista_itens(request):
    itens = Item.objects.select_related('categoria', 'localizacao', 'autor').order_by('-data')
    categorias = Categoria.objects.all()

    tipo = request.GET.get('tipo')
    if tipo in ('perdido', 'encontrado'):
        itens = itens.filter(tipo=tipo)

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        itens = itens.filter(categoria_id=categoria_id)

    status = request.GET.get('status')
    if status in ('aberto', 'resolvido'):
        itens = itens.filter(status=status)

    return render(request, 'itens/lista.html', {
        'itens': itens,
        'categorias': categorias,
        'tipo_atual': tipo,
        'categoria_atual': categoria_id,
        'status_atual': status,
    })


@login_required
def detalhe_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'itens/detalhe.html', {'item': item})


@login_required
def registrar_item(request):
    categorias = Categoria.objects.all()
    localizacoes = Localizacao.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        tipo = request.POST.get('tipo', '')
        categoria_id = request.POST.get('categoria') or None
        localizacao_id = request.POST.get('localizacao') or None
        foto = request.FILES.get('foto')

        # Criação rápida de categoria
        nova_categoria = request.POST.get('nova_categoria', '').strip()
        if nova_categoria and len(nova_categoria) >= 3:
            cat = Categoria.objects.filter(nome__iexact=nova_categoria).first()
            if not cat:
                cat = Categoria.objects.create(nome=nova_categoria)
            categoria_id = cat.pk

        # Criação rápida de localização
        nova_localizacao = request.POST.get('nova_localizacao', '').strip()
        if nova_localizacao and len(nova_localizacao) >= 3:
            loc = Localizacao.objects.filter(nome__iexact=nova_localizacao).first()
            if not loc:
                loc = Localizacao.objects.create(nome=nova_localizacao)
            localizacao_id = loc.pk

        erros = {}
        if len(titulo) < 5:
            erros['titulo'] = 'O título deve ter pelo menos 5 caracteres.'
        if len(descricao) < 10:
            erros['descricao'] = 'A descrição deve ter pelo menos 10 caracteres.'
        if tipo not in ('perdido', 'encontrado'):
            erros['tipo'] = 'Selecione um tipo válido.'

        if not erros:
            item = Item(
                titulo=titulo,
                descricao=descricao,
                tipo=tipo,
                status='aberto',
                autor=request.user,
                categoria_id=categoria_id,
                localizacao_id=localizacao_id,
            )
            if foto:
                item.foto = foto
            item.save()
            return redirect('detalhe_item', pk=item.pk)

        # Recarrega listas atualizadas (pode ter criado novos)
        categorias = Categoria.objects.all()
        localizacoes = Localizacao.objects.all()

        return render(request, 'itens/registrar.html', {
            'categorias': categorias,
            'localizacoes': localizacoes,
            'erros': erros,
            'post': request.POST,
        })

    return render(request, 'itens/registrar.html', {
        'categorias': categorias,
        'localizacoes': localizacoes,
    })


@login_required
def resolver_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.user != item.autor:
        return HttpResponseForbidden()
    if request.method == 'POST' and item.status == 'aberto':
        item.status = 'resolvido'
        item.save()
    return redirect('detalhe_item', pk=item.pk)
