from django.shortcuts import render, get_object_or_404
from .models import Grupo, Publicacion
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PublicacionForm, ComentarioForm 
from django.contrib.auth.forms import UserCreationForm # Importar el formulario de registro
from django.contrib.auth import login # Para loguear al usuario después del registro
from django.contrib.auth.models import User # Importar el modelo de usuario
from .forms import PublicacionForm, ComentarioForm, RegistroUsuarioForm # Importar el formulario de registro personalizado
from django.contrib.admin.views.decorators import staff_member_required # Para vistas de administración
from .forms import PublicacionForm, ComentarioForm, RegistroUsuarioForm, GrupoForm # Importar el formulario de registro personalizado y GrupoForm

# Vista para la página de inicio (Lista de grupos)
def lista_grupos(request):
    grupos = Grupo.objects.all().order_by('-fecha_creacion')
    return render(request, 'comunidad/lista_grupos.html', {'grupos': grupos})

# --- MODIFICAR ESTA VISTA EXISTENTE ---
@login_required
def detalle_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    publicaciones = grupo.publicaciones.all()
    
    # Verificar si el usuario actual ya es miembro
    es_miembro = request.user in grupo.miembros.all()

    # Lógica para publicar (Solo si es miembro)
    if request.method == 'POST' and es_miembro:
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.grupo = grupo
            post.save()
            return redirect('detalle_grupo', grupo_id=grupo.id)
    else:
        form = PublicacionForm()

    return render(request, 'comunidad/detalle_grupo.html', {
        'grupo': grupo, 
        'publicaciones': publicaciones,
        'form': form,
        'es_miembro': es_miembro 
    })

# --- AGREGAR ESTA NUEVA VISTA AL FINAL ---
@login_required
def detalle_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    comentarios = publicacion.comentarios.filter(parent=None) # Solo comentarios principales

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = publicacion
            comentario.save()
            return redirect('detalle_publicacion', publicacion_id=publicacion.id)
    else:
        form = ComentarioForm()

    return render(request, 'comunidad/detalle_publicacion.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'form': form
    })

# Vista para registrar nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_grupos')
    else:
        form = RegistroUsuarioForm() 
    
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def unirse_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    grupo.miembros.add(request.user) # Agrega al usuario a la lista
    return redirect('detalle_grupo', grupo_id=grupo.id)

@login_required
def salir_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    grupo.miembros.remove(request.user) # Saca al usuario de la lista
    return redirect('detalle_grupo', grupo_id=grupo.id)

@staff_member_required # Solo permite acceso si es Admin/Staff
def expulsar_miembro(request, grupo_id, usuario_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    usuario_a_expulsar = get_object_or_404(User, id=usuario_id)
    
    # Lo sacamos de la lista de miembros
    grupo.miembros.remove(usuario_a_expulsar)
    
    return redirect('detalle_grupo', grupo_id=grupo.id)

@staff_member_required
def eliminar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    grupo_id = publicacion.grupo.id # Guardamos el ID para volver
    
    # Borramos el post de la base de datos
    publicacion.delete()
    
    return redirect('detalle_grupo', grupo_id=grupo_id)

@login_required
def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            nuevo_grupo = form.save()

            # Opcional: Unir automáticamente al creador como miembro
            nuevo_grupo.miembros.add(request.user)

            return redirect('lista_grupos')
    else:
        form = GrupoForm()

    return render(request, 'comunidad/crear_grupo.html', {'form': form})

@staff_member_required # Importante: Solo el Admin puede hacer esto
def eliminar_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    grupo.delete() # Esto borra el grupo y todas sus publicaciones
    return redirect('lista_grupos')
