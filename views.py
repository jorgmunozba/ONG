from core.forms import MascotaForm
from django.shortcuts import render,redirect


from .models import Mascota
# Create your views here.

#inicio
def Index(request):
    return render(request, 'core/Index.html')

#donde estamos
def Donde_estamos(request):
    return render(request,'core/Donde_estamos.html')

#perros general
def Perros(request):
    mascotas = Mascota.objects.all().filter(idTipo_mascota=1)
    datos = {
        'perros': mascotas
    }
    if len(mascotas) > 0:
        datos['mensaje'] = "true"
    else:
        datos['mensaje'] = "false"

    return render(request, 'core/Perros.html', datos)

#gatos general
def Gatos(request):
    mascotas = Mascota.objects.all().filter(idTipo_mascota=2)
    datos = {
        'gatos': mascotas
    }

    if len(mascotas) > 0:
        datos['mensaje'] = "true"
    else:
        datos['mensaje'] = "false"

    return render(request, 'core/Gatos.html', datos)

#nosotros
def Nosotros(request):
    return render(request,'core/Nosotros.html')

#contacto
def Contacto(request):
    return render(request,'core/Contacto.html')

#form adopcion
def Adopcion(request, id):
    mascota = Mascota.objects.get(id_mascota = id)
    datos = {
        'mascota' : mascota
    }

    return render(request,'core/Adopcion.html', datos)

#panel control
def home(request):
    mascotas = Mascota.objects.all()
    datos = {
        'mascotas': mascotas
    }
    return render(request,'core/home.html', datos)

#form registro animal
def form_ong(request):
    datos= {
            'form': MascotaForm()
        }
    try:
        if request.method == 'POST':
            formulario = MascotaForm(request.POST, request.FILES)
            if formulario.is_valid:
                formulario.save()
                datos['mensaje'] = 'true'
    except:
        datos['mensaje'] = 'false'
    return render(request, 'core/form_ong.html', datos)

#form modificar animal
def form_mod_ong(request,id):
    mascotas = Mascota.objects.get(id_mascota = id)
    datos= {
        'form': MascotaForm(instance=mascotas)
    }
    try:
        if request.method == 'POST':
            formulario = MascotaForm(data=request.POST,instance=mascotas)
            if formulario.is_valid:
                formulario.save()
                datos['mensaje'] = "true"
    except:
        datos['mensaje'] = "false"
    return render(request, 'core/form_mod_ong.html', datos)

#eliminar mascota
def delete_ong(request,id):
    mascota = Mascota.objects.get(id_mascota = id)
    datos = {}
    try:
        datos['mensaje'] = "true"
        mascota.delete()
    except:
        datos['mensaje'] = "false"
    return render(request, 'core/home.html', datos)

