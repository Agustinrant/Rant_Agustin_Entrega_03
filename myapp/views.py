from django.shortcuts import render
from .models import JewelryPiece
from .forms import JewelryPieceForm

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
    query = request.GET.get('query', '')  # Recupera el término de búsqueda
    pieces = JewelryPiece.objects.filter(name__icontains=query) if query else []
    return render(request, 'myapp/search_piece.html', {'pieces': pieces, 'query': query})



def index(request):
    return render(request, 'myapp/index.html')


from django.shortcuts import render

def about(request):
    return render(request, 'myapp/about.html', {
        'name': 'Agustín Rant',
        'description': 'Soy Agustín Rant, artista con más de 10 años de experiencia en pintura al óleo y fundador de Occelo, un emprendimiento de joyería inspirado en la naturaleza.',
        'project': 'Occelo es una marca de joyería artesanal que combina diseño y arte para crear piezas únicas. Este proyecto es parte de mi pasión por el arte y la creatividad.',
        'photo_url': 'myapp/assets/img/agustin.jpg',  # Ruta actualizada de la foto
    })