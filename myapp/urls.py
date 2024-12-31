

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('create/', views.create_piece, name='create_piece'),  # Crear pieza
    path('search/', views.search_piece, name='search_piece'),  # Buscar piezas
    path('about/', views.about, name='about'),  # Acerca de mí
]


