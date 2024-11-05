# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import path, include, re_path
from appportfolio import views
from appportfolio.views import *

# servicio de ficheros estáticos durante el desarrollo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# servicio de ficheros estáticos durante el servidor
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar/', views.navbar, name='navbar'),
    re_path(r'^$', views.home,name='home'),
    re_path('habilidades', views.habilidades,name='habilidades'),
    path('agregarHabilidad', views.agregarHabilidad, name='agregarHabilidad'),
    re_path(r'^(?P<id>\d+)/modificarHabilidad$', views.modificarHabilidad,name='modificarHabilidad'),
    re_path(r'^(?P<id>\d+)/ver_habilidad$', views.ver_habilidad,name='ver_habilidad'),
    path('eliminarHabilidad/<int:pk>/', views.eliminarHabilidad, name='eliminarHabilidad'),
    re_path('sobremi', views.sobremi,name='sobremi'),
    re_path('categorias', views.categorias,name='categorias'),
    re_path('estudios', views.estudios,name='estudios'),
    re_path('experiencias', views.experiencias, name='experiencias'),
    # El primer parametro es el nombre de la vista que saldra en la ruta y 
    # el segundo parametro es el nombre de la funcion que se ejecutara, y 
    # el tercero parametro es el nombre de que se pondra en el template para llamar a la url
    re_path(r'^(?P<id>\d+)/ver_experiencia$', views.ver_experiencia,name='ver_experiencia'),
    path('eliminarExperiencia/<int:pk>/', views.eliminarExperiencia,name='eliminarExperiencia'),
    # re_path('entrevistadores', views.entrevistadores,name='entrevistadores'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('subirImagen/', views.subirImagen, name='subirImagen'),
    path('editarImagen/<int:imagen_id>/', views.editarImagen, name='editarImagen'),
    path('eliminarImagen/<int:imagen_id>/', views.eliminarImagen, name='eliminarImagen'),
    path('subirVideo/', views.subirVideo, name='subirVideo'),
    path('editarVideo/<int:video_id>/', views.editarVideo, name='editarVideo'),
    path('eliminarVideo/<int:video_id>/', views.eliminarVideo, name='eliminarVideo'),
    
    #re_path(r'^login/$', views.login, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
]