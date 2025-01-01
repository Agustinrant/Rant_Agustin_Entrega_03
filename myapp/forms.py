# from django import forms
# from .models import JewelryPiece

# class JewelryPieceForm(forms.ModelForm):
#     class Meta:
#         model = JewelryPiece 
#         fields = '__all__'  
        
        
# class JewelryPieceForm(forms.ModelForm):
#     class Meta:
#         model = JewelryPiece
#         fields = '__all__'
#         labels = {
#             'name': 'Nombre de la pieza',
#             'category': 'Categoría',
#             'material': 'Material',
#             'year_created': 'Año de creación',
#         }
#         help_texts = {
#             'year_created': 'Introduce el año en que fue creada la pieza.',
#         }
#         widgets = {
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'material': forms.Select(attrs={'class': 'form-control'}),
#             'year_created': forms.NumberInput(attrs={'class': 'form-control'}),
#         }
        
        
        
        
        
        


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import JewelryPiece

# Formulario para crear y editar piezas de joyería (ya existente)
class JewelryPieceForm(forms.ModelForm):
    class Meta:
        model = JewelryPiece
        fields = ['name', 'category', 'material', 'year_created']

# Nuevo formulario para registrar usuarios
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Campo adicional para el correo electrónico

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Campos del formulario