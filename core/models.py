from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'

class Item(models.Model):
    TIPO_CHOICES = [('perdido', 'Perdido'), ('encontrado', 'Encontrado')]
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

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
