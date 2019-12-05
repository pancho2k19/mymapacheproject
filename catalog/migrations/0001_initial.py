# Generated by Django 2.2.7 on 2019-12-04 21:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para el autor', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('informacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para la comuna', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para la region', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para el tipo', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(help_text='Rut único para el usuario', max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('reputacion', models.CharField(choices=[('e', 'pesima '), ('d', 'deficiente'), ('c', 'normal'), ('b', 'buena'), ('a', 'muy buena'), ('n/a', 'sin calificar')], default='n/a', max_length=3)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para la pieza', primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(max_length=50, upload_to='C:%Users%pancho%Desktop%proyecto_semestral_django%locallibreria%imagentest')),
                ('descripcion', models.CharField(max_length=100)),
                ('id_autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Autor')),
                ('id_tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Tipo')),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Region'),
        ),
    ]
