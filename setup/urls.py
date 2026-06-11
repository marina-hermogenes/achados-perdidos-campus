from django.contrib import admin
from django.urls import path
from django.conf import settings
from core import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('', views.home, name='home'),
    path('itens/', views.lista_itens, name='lista_itens'),
    path('itens/novo/', views.registrar_item, name='registrar_item'),
    path('itens/<int:pk>/', views.detalhe_item, name='detalhe_item'),
    path('itens/<int:pk>/resolver/', views.resolver_item, name='resolver_item'),
    path('perfil/', views.perfil, name='perfil'),
    path('itens/<int:pk>/editar/', views.editar_item, name='editar_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
