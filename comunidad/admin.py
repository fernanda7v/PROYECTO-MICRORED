from django.contrib import admin
from .models import Grupo, Publicacion, Comentario

# Configuración para el modelo Grupo
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre',)

# Configuración para el modelo Publicacion
@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'grupo', 'autor', 'fecha_publicacion')
    list_filter = ('grupo', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')

# Configuración para el modelo Comentario
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'publicacion', 'fecha_comentario', 'parent')
    list_filter = ('fecha_comentario',)