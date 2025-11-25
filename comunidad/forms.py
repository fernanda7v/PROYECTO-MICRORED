from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion, Comentario
from .models import Grupo, Publicacion, Comentario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos automáticamente
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

# 2. Formulario de Publicación
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de tu noticia'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '¿Qué está pasando?'}),
        }

# 3. Formulario de Comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Escribe un comentario...'}),
        }

# 4. Formulario para Crear Nuevo Grupo
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Vecinos de la Calle 10'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe de qué trata este grupo...'}),
        }