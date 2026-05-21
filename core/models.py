from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    def clean(self):
        # Mínimo de 3 caracteres
        if len(self.nome.strip()) < 3:
            raise ValidationError({'nome': 'O nome da categoria deve ter pelo menos 3 caracteres.'})

        # Nome não pode ser composto só de números
        if self.nome.strip().isdigit():
            raise ValidationError({'nome': 'O nome da categoria não pode ser composto apenas por números.'})

        # Sem duplicatas (ignora maiúsculas/minúsculas), excluindo o próprio registro na edição
        duplicata = Categoria.objects.filter(nome__iexact=self.nome.strip())
        if self.pk:
            duplicata = duplicata.exclude(pk=self.pk)
        if duplicata.exists():
            raise ValidationError({'nome': f'Já existe uma categoria com o nome "{self.nome.strip()}".'})

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Localizacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def clean(self):
        # Mínimo de 3 caracteres
        if len(self.nome.strip()) < 3:
            raise ValidationError({'nome': 'O nome da localização deve ter pelo menos 3 caracteres.'})

        # Sem duplicatas (ignora maiúsculas/minúsculas), excluindo o próprio registro na edição
        duplicata = Localizacao.objects.filter(nome__iexact=self.nome.strip())
        if self.pk:
            duplicata = duplicata.exclude(pk=self.pk)
        if duplicata.exists():
            raise ValidationError({'nome': f'Já existe uma localização com o nome "{self.nome.strip()}".'})

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'


class Item(models.Model):
    TIPO_CHOICES   = [('perdido', 'Perdido'), ('encontrado', 'Encontrado')]
    STATUS_CHOICES = [('aberto', 'Aberto'), ('resolvido', 'Resolvido')]

    titulo      = models.CharField(max_length=100)
    descricao   = models.TextField()
    tipo        = models.CharField(max_length=10, choices=TIPO_CHOICES)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')
    categoria   = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True)
    autor       = models.ForeignKey(User, on_delete=models.CASCADE)
    data        = models.DateTimeField(auto_now_add=True)
    foto        = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f"[{self.tipo}] {self.titulo}"

    def clean(self):
        # Título com no mínimo 5 caracteres
        if len(self.titulo.strip()) < 5:
            raise ValidationError({'titulo': 'O título deve ter pelo menos 5 caracteres.'})

        # Descrição com no mínimo 10 caracteres
        if len(self.descricao.strip()) < 10:
            raise ValidationError({'descricao': 'A descrição deve ter pelo menos 10 caracteres.'})

        # Item resolvido exige descrição mais detalhada (mínimo 20 caracteres)
        if self.status == 'resolvido' and len(self.descricao.strip()) < 20:
            raise ValidationError({
                'descricao': 'Para marcar um item como resolvido, a descrição deve ter pelo menos 20 caracteres.'
            })

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
