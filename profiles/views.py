from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user  # Obtiene el usuario autenticado
    return render(request, 'profiles/profile.html', {'user': user})



def detail_piece(request, piece_id):
    # Obtén la pieza específica o lanza un error 404 si no existe
    piece = get_object_or_404(JewelryPiece, id=piece_id)
    return render(request, 'myapp/detail_piece.html', {'piece': piece})
