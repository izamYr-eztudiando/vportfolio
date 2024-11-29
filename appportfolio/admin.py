# -*- coding: utf-8 -*-
from django.contrib import admin
from appportfolio.models import *
from django.contrib.auth.models import User 


admin.site.site_header = "Sitio web Salmantino"  #este es el título
admin.site.site_title = "Portal de Saludos"
admin.site.index_title = "Bienvenidos al portal de Administración"


class HabilidadAdmin(admin.ModelAdmin):
	list_display = [co.name for co in Habilidad._meta.get_fields()]
	search_fields = ('id','habilidad') #siempre tienen que ser una tupla
	list_filter   = ('id','habilidad') #siempre tienen que ser una tupla
admin.site.register(Habilidad, HabilidadAdmin)

class PersonalAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Personal._meta.get_fields()]
    search_fields = ('id','nombre', 'apellido1', 'apellido2', 'edad')
    list_filter = ('id','nombre', 'apellido1', 'apellido2', 'edad')
admin.site.register(Personal, PersonalAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Categoria._meta.get_fields()]
    search_fields = ('id','nombre_categoria')
    list_filter = ('id','nombre_categoria')
admin.site.register(Categoria, CategoriaAdmin)

class EstudioAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Estudio._meta.get_fields()]
    search_fields = ('id','titulacion','fechaInicio','fechaFin','notaMedia','lugarEstudio','nombreLugar','ciudad','presencial','observaciones')
    list_filter = ('id','titulacion','fechaInicio','fechaFin','notaMedia','lugarEstudio','nombreLugar','ciudad','presencial','observaciones')
admin.site.register(Estudio, EstudioAdmin)
# Register your models here.

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Experiencia._meta.get_fields()] #Esto es un forEach que va a recorrer cada campo de la clase
    search_fields = ('id','empresa','fecha_inicio','fecha_fin','observaciones','categoria')
    list_filter = ('id','empresa','categoria')
admin.site.register(Experiencia, ExperienciaAdmin)

class EntrevistadorAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Entrevistador._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id','empresa')
admin.site.register(Entrevistador, EntrevistadorAdmin)

class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','imagen','comentario')
admin.site.register(Imagen, ImagenAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','video','comentario')
admin.site.register(Video, VideoAdmin)

class CurriculumAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Curriculum._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id','nombre','apellido1','apellido2','email','telefono')
    list_filter = ('id','nombre','apellido1','apellido2','email','telefono')
admin.site.register(Curriculum, CurriculumAdmin)

class DetalleCurriculumEstudioAdmin(admin.ModelAdmin):
    list_display = [co.name for co in DetalleCurriculumEstudio._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id', 'estudios', 'curriculum')
admin.site.register(DetalleCurriculumEstudio, DetalleCurriculumEstudioAdmin)

class DetalleCurriculumExperienciaAdmin(admin.ModelAdmin):
    list_display = [co.name for co in DetalleCurriculumExperiencia._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id', 'experiencias', 'curriculum')
admin.site.register(DetalleCurriculumExperiencia, DetalleCurriculumExperienciaAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Noticia._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id','titulo','contenido','fecha_creacion','imagen')
admin.site.register(Noticia, NoticiaAdmin)

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Valoracion._meta.get_fields() if hasattr(co, 'verbose_name')]
    readonly_fields = ('media_aspectos',)

    def save_model(self, request, obj, form, change):
        # Calcula automáticamente la media
        if obj.votos_entrevista and obj.votos_empresa:
            obj.media_aspectos = (obj.votos_entrevista + obj.votos_empresa) / 2
        super().save_model(request, obj, form, change)

class EstadoAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Estado._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id','estado')
admin.site.register(Estado, EstadoAdmin)

class TareasAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Tareas._meta.get_fields() if hasattr(co, 'verbose_name')]
    search_fields = ('id','tarea','fecha','estado')
admin.site.register(Tareas, TareasAdmin)