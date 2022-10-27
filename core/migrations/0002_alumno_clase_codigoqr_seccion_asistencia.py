# Generated by Django 4.0.4 on 2022-09-06 19:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('alumnoId', models.BigAutoField(primary_key=True, serialize=False)),
                ('alumnoRut', models.IntegerField(unique=True)),
                ('alumnoDv', models.CharField(max_length=1)),
                ('alumnoNombre', models.CharField(max_length=200)),
                ('alumnoUser', models.CharField(max_length=40)),
                ('alumnoPass', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('claseId', models.BigAutoField(primary_key=True, serialize=False)),
                ('claseDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='CodigoQR',
            fields=[
                ('codigoId', models.BigAutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=500, null=True)),
                ('fechaexp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('seccionId', models.BigAutoField(primary_key=True, serialize=False)),
                ('seccionNum', models.IntegerField()),
                ('seccionTipo', models.CharField(choices=[('D', 'Diurno'), ('V', 'Vespertino')], max_length=1)),
                ('seccionProfesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesor')),
                ('seccionRamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ramo')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('asistenciaId', models.BigAutoField(primary_key=True, serialize=False)),
                ('presente', models.BooleanField(default=False)),
                ('asistenciaAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
                ('asistenciaClase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clase')),
            ],
        ),
    ]
