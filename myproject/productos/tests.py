from django.test import TestCase
from django.urls import reverse

class ProductoTests(TestCase):
    def test_registrar_url(self):
        #Ejercicio 1.- Verificación del funcionamiento de la URL: registrar/, que devuelva un código de estatus 200.
        response = self.client.get('/registrar/')
        self.assertEqual(response.status_code, 200)

    def test_url_reverse_name_registrar_producto(self):
        #Ejercicio 2.- Prueba de validación de URL disponible por nombre del enlace reverso de: registrar_producto.
        try:
            url = reverse('registrar_producto')
            self.assertTrue(url)
        except Exception as e:
            self.fail(f"Reverse for 'registrar_producto' failed: {str(e)}")

    def test_template_name_correctness(self):
        #Ejercicio 3.- Verificar si el nombre es correcto con relación a la plantilla de insertar (registrar_producto.html) y su nombre reverso.
        response = self.client.get(reverse('registrar_producto'))
        self.assertTemplateUsed(response, 'productos/registrar_producto.html')

    def test_template_content_producto_list(self):
        #Ejercicio 4.- 4. Verificar si un contenido corresponde a la plantilla (producto_list.html), por ejemplo: "<th>Nombre</th>”.
        response = self.client.get(reverse('producto_list'))
        self.assertContains(response, '<th>Nombre</th>')
