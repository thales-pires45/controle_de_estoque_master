"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('projeto.usuarios.urls')),
    path('core/', include('projeto.core.urls')),
    path("", lambda request: redirect('/auth/login/')),
    path('produto/', include('projeto.produto.urls')),
    path('cliente/', include('projeto.cliente.urls')),
    path('entrada/', include('projeto.entrada.urls')),
    path('saida/', include('projeto.saida.urls')),
    path('relatorio/', include('projeto.relatorio.urls')),

]
