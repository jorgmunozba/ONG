from django import forms
from django.forms import ModelForm

from .models import Mascota 

class MascotaForm (ModelForm):  

    class Meta:
        model = Mascota
        fields = ['nombre','edad','esterilizado', 'idTipo_mascota', 'imagen', 'nroChip', 'genero']
        widgets = {
            'nroChip' : forms.NumberInput({'placeholder' : '1111111111'}),
            'nombre' : forms.TextInput({'placeholder' : ' Cachulo'}),
            'imagen' : forms.FileInput(), 
            'esterilizado' : forms.CheckboxInput,
            'genero' : forms.Select(),
            'idTipo_mascota' : forms.Select()
        }

    def __init__(self, *args, **kwargs): 
        super(MascotaForm, self).__init__(*args, **kwargs) 
        self.fields['idTipo_mascota'].empty_label = "Seleccione tipo mascota" 
        self.fields['genero'].empty_label = "Seleccione género" 