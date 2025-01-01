from django.shortcuts import render
from .models import JewelryPiece
from .forms import JewelryPieceForm
from django.shortcuts import redirect, get_object_or_404

def create_piece(request):
    if request.method == 'POST':
        form = JewelryPieceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html', {'message': 'Pieza creada exitosamente!'})
    else:
        form = JewelryPieceForm()
    return render(request, 'myapp/create_piece.html', {'form': form})

def search_piece(request):
    # Recuperar términos de búsqueda desde la solicitud
    query = request.GET.get('query', '')  # Búsqueda por nombre
    category = request.GET.get('category', '')  # Búsqueda por categoría
    material = request.GET.get('material', '')  # Búsqueda por material
    year = request.GET.get('year', '')  # Búsqueda por año de creación

    # Filtrar las piezas en la base de datos
    pieces = JewelryPiece.objects.all()

    if query:
        pieces = pieces.filter(name__icontains=query)
    if category:
        pieces = pieces.filter(category__iexact=category)
    if material:
        pieces = pieces.filter(material__iexact=material)
    if year:
        pieces = pieces.filter(year_created=year)

    # Renderizar la plantilla con los resultados y los filtros actuales
    return render(request, 'myapp/search_piece.html', {
        'pieces': pieces,
        'query': query,
        'category': category,
        'material': material,
        'year': year,
    })


def index(request):
    return render(request, 'myapp/index.html')



def about(request):
    return render(request, 'myapp/about.html', {
        'name': 'Agustín Rant',
        'description': 'Soy Agustín Rant, artista con más de 10 años de experiencia en pintura al óleo y fundador de Occelo, un emprendimiento de joyería inspirado en la naturaleza.',
        'project': 'Occelo es una marca de joyería artesanal que combina diseño y arte para crear piezas únicas. Este proyecto es parte de mi pasión por el arte y la creatividad.',
        'photo_url': 'myapp/assets/img/agustin.jpg',  # Ruta actualizada de la foto
    })
    

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import JewelryPiece

@login_required
def delete_piece(request, piece_id):
    # Obtener la pieza por ID o devolver 404 si no existe
    piece = get_object_or_404(JewelryPiece, id=piece_id)

    # Eliminar la pieza
    piece.delete()

    # Redirigir a la página de búsqueda
    return redirect('search_piece')

@login_required
def edit_piece(request, piece_id):
    # Obtener la pieza por ID o lanzar un 404 si no existe
    piece = get_object_or_404(JewelryPiece, id=piece_id)

    if request.method == 'POST':
        # Si se envía el formulario, actualizar la pieza
        form = JewelryPieceForm(request.POST, instance=piece)
        if form.is_valid():
            form.save()
            return redirect('search_piece')  # Redirigir a la búsqueda tras guardar
    else:
        # Si es GET, cargar el formulario con los datos existentes
        form = JewelryPieceForm(instance=piece)

    return render(request, 'myapp/edit_piece.html', {'form': form, 'piece': piece})

from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login tras el registro
    else:
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

# eso corresponde a "VER MAS"
def detail_piece(request, piece_id):
    # Obtén la pieza específica o lanza un error 404 si no existe
    piece = get_object_or_404(JewelryPiece, id=piece_id)
    return render(request, 'myapp/detail_piece.html', {'piece': piece})