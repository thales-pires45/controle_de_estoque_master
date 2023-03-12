from django.urls import path

from projeto.core import views

app_name = 'core'

urlpatterns = [
    path('home/', views.index, name='index'),
]