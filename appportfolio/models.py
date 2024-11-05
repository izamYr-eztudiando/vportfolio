# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cgi import maxlen

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
################################################
# Habilidades 
################################################


class Habilidad(models.Model):  
    id = models.AutoField(primary_key=True)
    habilidad = models.CharField("Nombre de Habilidad",max_length=25, null=True, blank=True)
    nivel = models.IntegerField("Nivel",null=True, blank=True) # 1 al 10
    comentario = models.TextField("Comentario", max_length=255, null=True, blank=True)
	
    class Meta:
        verbose_name = "Habilidad"  #puede ser otro nombre
        verbose_name_plural = "Habilidades"
        ordering = ['habilidad']
        
    def __str__(self):
        return '%s,%s' % (self.habilidad, self.nivel)


class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=25, null=True, blank=True)
    apellido1 = models.CharField("Primer apellido", max_length=25, null=True, blank=True)
    apellido2 = models.CharField("Segundo apellido", max_length=25, null=True, blank=True)
    edad = models.IntegerField("Edad", null=True, blank=True)
    usuario = models.ForeignKey(User, related_name='datos_usuario', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Personal" 
        verbose_name_plural = "Personales"
        ordering = ['nombre']
    
    def __str__(self):
        return '%s,%s,%s,%s,%s' % (self.id, self.nombre, self.apellido1, self.apellido2, self.edad)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField("Nombre de la categoria", max_length=25, null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre_categoria']

    def __str__(self):
        return '%s,%s' % (self.nombre_categoria, self.id)

class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    titulacion = models.CharField("Titulo", max_length=25, null=True, blank=True)
    fechaInicio = models.DateField("Fecha Inicio", null=True, blank=True)
    fechaFin = models.DateField("Fecha Final", null=True, blank=True)
    notaMedia = models.FloatField("Nota Media", null=True, blank=True)
    lugarEstudio = models.CharField("Lugar Estudio", max_length=45, null=True, blank=True)
    nombreLugar = models.CharField("Nombre Lugar", max_length=25, null=True, blank=True)
    ciudad = models.CharField("Ciudad", max_length=25, null=True, blank=True)
    presencial = models.BooleanField("Presencial", null=True, blank=True)
    observaciones = models.TextField("Observaciones", null=True, blank=True)

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
        ordering = ['id']

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (self.id, self.titulacion, self.fechaInicio, self.fechaFin, self.notaMedia, self.lugarEstudio, self.nombreLugar, self.ciudad, self.presencial, self.observaciones)

class Experiencia(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField("Empresa", max_length=50, null=True, blank=True)
    fecha_inicio = models.DateField("Fecha de Inicio", null=True, blank=True)
    fecha_fin = models.DateField("Fecha de Finalización", null=True, blank=True)
    observaciones = models.CharField("Funciones", max_length=50, null=True, blank=True)
    #categoria = models.ForeignKey(Categoria, related_name='expe_categoria', null=True, blank=True, on_delete=models.PROTECT)
    categoria = models.CharField("Categoria", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['empresa']

    def __str__(self):
        return '%s,%s' % (self.empresa, self.fecha_inicio)

# class Imagen(models.Model):
#     id = models.AutoField(primary_key=True)
#     imagen = models.ImageField('Imagen', blank=True, null=True, upload_to='media/')
#     estudio = models.ForeignKey(Estudio, related_name='imagenes_estudio', null=True, blank=True, on_delete=models.PROTECT)
    
#     class Meta:
#         verbose_name = "Imagen"
#         verbose_name_plural = "Imagenes"
#         ordering = ['id']
    
#     def __str__(self):
#         return '%s,%s' % (self.imagen, self.estudio)

class Entrevistador(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField('Avatar', blank=True, null=True, upload_to='media/')
    empresa = models.CharField("Empresa", max_length=30, null=True, blank=True)
    fecha_entrevista = models.DateField("Fecha de Entrevista", null=True, blank=True)
    conectado = models.BooleanField("Conectado", null=True, blank=True)
    seleccionado = models.BooleanField("Seleccionado", null=True, blank=True)
    # foreign keys requerido desde django 2.0
    user = models.ForeignKey(User, related_name='entrevistados_usuarios', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Entrevistador" #Esto es el nombre que se verá en la pantalla de administración de Django
        verbose_name_plural = "Entrevistadores"
        ordering = ['empresa']
    
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id, self.empresa, self.fecha_entrevista, self.conectado, self.seleccionado, self.user)
    
class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField('Imagen', blank=True, null=True, upload_to='imagenes/')
    comentario = models.CharField("Comentario", max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['id']

    def __str__(self):
        return '%s,%s,%s' % (self.id, self.imagen, self.comentario)
    
class Video (models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField('Video', blank=True, null=True, upload_to='videos/')
    comentario = models.CharField("Comentario", max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['id']

    def __str__(self):
        return '%s,%s,%s' % (self.id, self.video, self.comentario)
    
