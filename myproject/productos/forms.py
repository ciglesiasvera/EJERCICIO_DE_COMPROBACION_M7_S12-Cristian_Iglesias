from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'f_vencimiento']
        widgets = {
            'f_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }