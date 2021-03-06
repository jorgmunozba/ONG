# Generated by Django 3.2.3 on 2021-06-26 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_mascota',
            fields=[
                ('idTipo_mascota', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Tipo mascota')),
                ('nombreTipo_mascota', models.CharField(max_length=50, verbose_name='Tipo mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='id mascota')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('edad', models.IntegerField(verbose_name='edad')),
                ('esterilizado', models.CharField(max_length=2, verbose_name='esterilizado')),
                ('imagen', models.ImageField(upload_to='mascotas', verbose_name='Imagen')),
                ('idTipo_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_mascota')),
            ],
        ),
    ]
