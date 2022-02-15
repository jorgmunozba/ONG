from django.db import models

# Create your models here.

class Tipo_mascota(models.Model):
    idTipo_mascota = models.IntegerField(primary_key = True, verbose_name='id de Tipo mascota')
    nombreTipo_mascota = models.CharField(max_length=50,verbose_name='Tipo mascota')

    def __str__(self):
        return self.nombreTipo_mascota

class GeneroMascota(models.Model):
    idGenero = models.AutoField(verbose_name='Id genero', primary_key=True)
    genero = models.CharField(verbose_name="Género", max_length=30)

    def __str__(self):
        return self.genero

class Mascota(models.Model):
    #id autoincrementable
    id_mascota = models.AutoField( primary_key=True,verbose_name='id mascota')
    nombre = models.CharField(max_length=20, verbose_name='nombre')
    edad = models.IntegerField(verbose_name='edad')
    idTipo_mascota = models.ForeignKey(Tipo_mascota, on_delete=models.CASCADE, verbose_name="Tipo mascota")
    esterilizado = models.BooleanField(max_length=2, verbose_name='esterilizado')
    #GUARDAR IMAGEN EN BD
    imagen = models.ImageField(verbose_name='Imagen', upload_to='mascotas', null=False)
    #GUARDAR NRO CHIP y unico
    nroChip = models.CharField(max_length=20, verbose_name='Nro Chip')
    #genero mascota
    genero = models.ForeignKey(GeneroMascota, on_delete=models.CASCADE, verbose_name="Género")


    def __str__(self):
        return self.nombre