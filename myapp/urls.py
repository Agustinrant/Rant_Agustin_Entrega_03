

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('create/', views.create_piece, name='create_piece'),  # Crear pieza
    path('search/', views.search_piece, name='search_piece'),  # Buscar piezas
    path('about/', views.about, name='about'),  # Acerca de mí
    path('delete/<int:piece_id>/', views.delete_piece, name='delete_piece'),  # Ruta para eliminar
    path('edit/<int:piece_id>/', views.edit_piece, name='edit_piece'),  # Ruta para editar
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
     path('detail/<int:piece_id>/', views.detail_piece, name='detail_piece'),
]




