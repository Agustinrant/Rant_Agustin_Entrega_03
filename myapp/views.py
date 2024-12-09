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