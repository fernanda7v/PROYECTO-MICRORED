from django.urls import path
from . import views

urlpatterns = [
    # Ruta vacía = Página de inicio
    path('', views.lista_grupos, name='lista_grupos'),
    
    # Ruta para ver un grupo específico (ej: /grupo/1/)
    path('grupo/<int:grupo_id>/', views.detalle_grupo, name='detalle_grupo'),

    path('publicacion/<int:publicacion_id>/', views.detalle_publicacion, name='detalle_publicacion'),

    path('registro/', views.registro, name='registro'),

    path('grupo/<int:grupo_id>/unirse/', views.unirse_grupo, name='unirse_grupo'),

    path('grupo/<int:grupo_id>/salir/', views.salir_grupo, name='salir_grupo'),

    path('grupo/<int:grupo_id>/expulsar/<int:usuario_id>/', views.expulsar_miembro, name='expulsar_miembro'),

    path('publicacion/<int:publicacion_id>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),

    path('nuevo-grupo/', views.crear_grupo, name='crear_grupo'),

    path('grupo/<int:grupo_id>/eliminar-grupo/', views.eliminar_grupo, name='eliminar_grupo'),
]
