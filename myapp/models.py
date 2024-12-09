from django.db import models

class JewelryPiece(models.Model):
    CATEGORY_CHOICES = [
        ('ANILLO', 'Anillo'),
        ('COLGANTE', 'Colgante'),
        ('ARO', 'Aro'),
    ]

    MATERIAL_CHOICES = [
        ('PLATA', 'Plata'),
        ('BRONCE', 'Bronce'),
        ('ORO', 'Oro'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    material = models.CharField(max_length=10, choices=MATERIAL_CHOICES)
    year_created = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.category})"