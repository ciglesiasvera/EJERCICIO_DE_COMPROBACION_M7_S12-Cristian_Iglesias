from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Fabrica, Producto

def obtener_fabricas_y_productos(request):
    fabricas = Fabrica.objects.raw('SELECT id, nombre FROM productos_fabrica')
    productos = Producto.objects.raw('''
        SELECT p.id, p.nombre, f.nombre as fabrica_nombre
        FROM productos_producto p
        JOIN productos_fabrica f ON p.fabrica_id = f.id
    ''')
    context = {
        'fabricas': fabricas,
        'productos': productos,
    }
    return render(request, 'productos/fabricas_y_productos.html', context)

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto_list.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/registrar_producto.html', {'form': form})