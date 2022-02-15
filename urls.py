from django.urls import path

from .views import *



urlpatterns = [
    #incio
    path('inicio/', Index, name="inicio"),

    #donde estamos
    path('donde-estamos/', Donde_estamos, name="donde_estamos"),

    #perros_general
    path('perros-adopcion/', Perros, name="perros"),

    #gatos_general
    path('gatos-adopcion/', Gatos,name="gatos"),

    #nosotros
    path('nosotros/',Nosotros,name="nosotros"),

    #contacto
    path('contacto/',Contacto,name="contacto"),

    #form adopcion
    path('formulario-adopcion/<id>', Adopcion, name="adopcion"),

    #panel de control
    path('mascotas-registradas/', home, name="panel_control"),

    #form add mascota
    path('registrar-mascota/', form_ong, name="agregar_mascota"),

    #form update mascota
    path('editar-mascota/<id>/', form_mod_ong, name="modificar_mascota"),

    #eliminar mascota
    path('eliminar-mascota/<id>/', delete_ong, name="delete_mascota"),
    
    
]

