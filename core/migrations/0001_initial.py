# Generated by Django 4.0.4 on 2022-09-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('profeId', models.BigAutoField(primary_key=True, serialize=False)),
                ('profeRut', models.IntegerField(unique=True)),
                ('profeDv', models.CharField(max_length=1)),
                ('profeNombre', models.CharField(max_length=200)),
                ('profeUser', models.CharField(max_length=40)),
                ('profePass', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('ramoId', models.BigAutoField(primary_key=True, serialize=False)),
                ('ramoLetra', models.CharField(max_length=4)),
                ('ramoNum', models.IntegerField()),
                ('ramoNombre', models.CharField(max_length=100)),
            ],
        ),
    ]
