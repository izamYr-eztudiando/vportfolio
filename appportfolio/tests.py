import os # Usado para interactuar con el sistema de archivos
from django.test import TestCase # Clase de Django para crear pruebas unitarias de

# Permite sobreescribir la configuración de la aplicación
from django.test import override_settings

from appportfolio.models import *

# Facilita la creación de archivos simulados que se pueden cargar en el modelo.
from django.core.files.uploadedfile import SimpleUploadedFile

from os.path import basename # Extrae el nombre base de un archivo (sin la ruta)
import tempfile # Usado para crear archivos temporales donde almacenar los archivos durante las pruebas
from uuid import uuid4 # Genera un identificador único

# decorador que cambia la ruta solo para pruebas
@override_settings(MEDIA_ROOT=tempfile.gettempdir())
class NoticiaModelTest(TestCase):
    def tearDown(self):
        # método especial de django para eliminar los archivos después de las pruebas
        for noticia in Noticia.objects.all():
            if noticia.imagen and os.path.exists(noticia.imagen.path):
                os.remove(noticia.imagen.path)

        super().tearDown()
    
    def test_creacion_noticia_sin_imagen(self):
        """ Prueba de que una noticia se puede crear sin imagen """
        noticia = Noticia.objects.create(
            titulo = "Noticia sin imagen",
            contenido = "Contenido de prueba sin imagen"
        )
        self.assertEqual(noticia.titulo, "Noticia sin imagen")
        self.assertEqual(noticia.contenido, "Contenido de prueba sin imagen")
        self.assertFalse(noticia.imagen) # Verificar que no haya imagen

    def test_creacion_noticia_con_imagen(self):
        """ Prueba de que una noticia se puede crear con imagen cargada"""
        unique_filename = f'test_image_{uuid4().hex}.jpg'
        image_data = SimpleUploadedFile(
            name = unique_filename,
            content = b'algun contenido de la imagen',
            content_type = 'image/jpeg'
        )
        noticia = Noticia.objects.create(
            titulo = "Noticia con imagen",
            contenido = "Contenido de prueba con imagen",
            imagen = image_data
        )
        self.assertEqual(noticia.titulo, "Noticia con imagen")
        self.assertEqual(noticia.contenido, "Contenido de prueba con imagen")
        self.assertIsNotNone(noticia.imagen) # La imagen no debería estar vacía
        # Comparar con el nombre dinámico generado
        self.assertEqual(basename(noticia.imagen.name), unique_filename)

# Create your tests here.