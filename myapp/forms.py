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
from .models import JewelryPiece

class JewelryPieceForm(forms.ModelForm):
    class Meta:
        model = JewelryPiece
        fields = ['name', 'category', 'material', 'year_created']