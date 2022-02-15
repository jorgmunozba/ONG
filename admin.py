from django.contrib import admin
from .models import GeneroMascota, Tipo_mascota, Mascota
# Register your models here.

admin.site.register(Tipo_mascota)
admin.site.register(Mascota)
admin.site.register(GeneroMascota)
