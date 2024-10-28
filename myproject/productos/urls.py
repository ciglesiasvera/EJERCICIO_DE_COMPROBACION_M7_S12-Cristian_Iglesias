from django.urls import path
from .views import producto_list, registrar_producto

urlpatterns = [
    path('', producto_list, name='producto_list'),
    path('registrar/', registrar_producto, name='registrar_producto'),
    path('productos/', producto_list, name='producto_list'),
]