# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    avatar= models.ImageField('Avatar', blank=True, null = True, upload_to="media/")
    empresa = models.CharField('Empresa',max_length=30,null=True, blank=True)
    fecha_entrevista= models.DateField('Fecha Entrevista',null=True, blank=True)
    conectado = models.BooleanField('Conectado',null=True, blank=True) 
    seleccionado = models.BooleanField('Seleccionado',null=True, blank=True) 
    # forteigns keys requerido desde django 2.0
    user = models.ForeignKey(User, related_name='entrevistados_usuario', 
    null=True, blank=True, on_delete=models.PROTECT)  

    class Meta:
        verbose_name = 'Entrevistador'  
        verbose_name_plural = 'Entrevistadores'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.id, self.empresa, self.fecha_entrevista, 
        self.conectado, self.seleccionado, self.user)   
    
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
    
class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=15, null=True, blank=True)
    apellido1 = models.CharField("Primer apellido", max_length=25, null=True, blank=True)
    apellido2 = models.CharField("Segundo apellido", max_length=25, null=True, blank=True)
    email = models.CharField("Email", max_length=200, null=True, blank=True)
    telefono = models.CharField("Telefono", max_length=9, null=True, blank=True)

    class Meta:
        verbose_name = "Curriculum" 
        verbose_name_plural = "Curriculums"
        ordering = ['nombre']
    
    def __str__(self):
        return '%s,%s,%s,%s,%s' % (self.id, self.nombre, self.apellido1, self.apellido2, self.email)
    
class DetalleCurriculumEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    estudios = models.ForeignKey(Estudio, related_name='detalle_estudios', null=True, blank=True, on_delete=models.PROTECT)
    curriculum = models.ForeignKey(Curriculum, related_name='detalle_curriculum_estudio', null=True, blank=True, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Detalle curriculum estudio" 
        verbose_name_plural = "Detalle curriculum estudios"
        ordering = ['estudios']
    
    def __str__(self):
        return '%s,%s,%s' % (self.id, self.estudios, self.curriculum)

class DetalleCurriculumExperiencia(models.Model):
    id = models.AutoField(primary_key=True)
    experiencias = models.ForeignKey(Experiencia, related_name='detalle_experiencias', null=True, blank=True, on_delete=models.PROTECT)
    curriculum = models.ForeignKey(Curriculum, related_name='detalle_curriculum_experiencia', null=True, blank=True, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Detalle curriculum experiencia" 
        verbose_name_plural = "Detalle curriculum experiencias"
        ordering = ['experiencias']
        
    def __str__(self):
        return '%s,%s,%s' % (self.id, self.experiencias, self.curriculum)
    
class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("Titulo", max_length=50, null=True, blank=True)
    contenido = models.TextField("Contenido")
    fecha_creacion = models.DateTimeField("Fecha de creacion", auto_now_add=True)
    imagen = models.ImageField("Imagen", null=True, blank=True, upload_to='noticias/')

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['id']

    def __str__(self):
        return '%s,%s,%s,%s,%s' % (self.id, self.titulo, self.contenido, self.fecha_creacion, self.imagen)
    
class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    votos_entrevista = models.DecimalField("Votos Entrevista", max_digits=3, decimal_places=1, null=True, blank=True)
    votos_empresa = models.DecimalField("Votos Empresa", max_digits=3, decimal_places=1, null=True, blank=True)
    media_aspectos = models.DecimalField("Media Aspectos", max_digits=3, decimal_places=1, null=True, blank=True)
    entrevista = models.CharField("Descrición Entrevista", max_length=200, null=True, blank=True)
    empresa = models.CharField("Descripción Empresa", max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField("Fecha", default=timezone.now)

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s' % (self.id, self.votos_entrevista, self.votos_empresa, self.media_aspectos, self.entrevista, self.empresa, self.timestamp)

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField('Contenido del mensaje')
    fecha_envio = models.DateTimeField('Fecha de envío', auto_now_add=True)
    leido = models.BooleanField('Leído', default=False)

    class Meta:
        ordering = ['fecha_envio']

    def __str__(self):
        return f"De: {self.remitente.username} Para: {self.destinatario.username} - {self.contenido[:30]}"
    
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField("Estado", max_length=25, null=True, blank=True)

    class Meta: 
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['estado']
    
    def __str__(self):
        return '%s' % (self.estado)
    
class Tareas(models.Model):
    id = models.AutoField(primary_key=True)
    tarea = models.CharField("Tarea", max_length=25, null=True, blank=True)
    fecha = models.DateField("Fecha", null=True, blank=True)
    estado = models.ForeignKey(Estado, related_name='tareas_estado', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['tarea']

    def __str__(self):
        return '%s,%s,%s,%s' % (self.id, self.tarea, self.fecha, self.estado)