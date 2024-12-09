from django.shortcuts import render


from django.shortcuts import render
from .forms import JewelryPieceForm

def create_piece(request):
    if request.method == 'POST':
        form = JewelryPieceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Redirige a una página de éxito
    else:
        form = JewelryPieceForm()
    return render(request, 'myapp/create_piece.html', {'form': form})