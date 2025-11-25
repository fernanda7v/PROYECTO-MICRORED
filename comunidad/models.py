from django.db import models
from django.contrib.auth.models import User

# 1. Modelo para los Grupos (ej: "Barrio Los Pinos", "Fútbol Domingos")
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    miembros = models.ManyToManyField(User, related_name='grupos_unidos', blank=True)

    def __str__(self):
        return self.nombre

# 2. Modelo para las Publicaciones (Posts)
class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='publicaciones')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordenar: las más nuevas primero
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f"{self.titulo} - por {self.autor.username}"

# 3. Modelo para Comentarios (con soporte para hilos/respuestas)
class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    # Este campo 'parent' permite que un comentario sea respuesta de otro
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')

    class Meta:
        ordering = ['fecha_comentario']

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"