# Generated by Django 2.0 on 2018-05-25 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_nombre', models.CharField(choices=[('Realista', 'REALISTA'), ('Investigativo', 'INVESTIGATIVO'), ('Social', 'SOCIAL'), ('Artista', 'ARTISTA'), ('Emprendedor', 'EMPRENDEDOR'), ('Convencional', 'CONVENCIONAL'), ('Manual', 'MANUAL'), ('Mecanica', 'MECANICA'), ('Cientifica', 'CIENTIFICA'), ('Percepcion_Espacial', 'PERCEPCION ESPACIAL'), ('Prosocial', 'PROSOCIAL'), ('Enseñanza', 'ENSEÑANZA'), ('Creativa_Artistica', 'CREATIVA_ARTISTICA'), ('Literaria', 'LITERARIA'), ('Liderazgo', 'LIDERAZGO'), ('Gerencial', 'GERENCIAL'), ('Organizacion', 'ORGANIZACION'), ('Manejo_de_Datos', 'MANEJO_DE_DATOS')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera_nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera_Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Area')),
                ('carrera_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Carrera_Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encuesta_tipo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion_nombre', models.CharField(max_length=50)),
                ('institucion_direccion', models.CharField(max_length=100)),
                ('institucion_correo', models.EmailField(max_length=254)),
                ('institucion_telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientador_nombre', models.CharField(max_length=35)),
                ('orientador_ap_paterno', models.CharField(max_length=35)),
                ('orientador_ap_materno', models.CharField(max_length=35)),
                ('orientador_edad', models.IntegerField()),
                ('orientador_sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('orientador_correo', models.EmailField(max_length=254)),
                ('orientador_area', models.CharField(blank=True, max_length=35, null=True)),
                ('orientador_slug', models.SlugField(max_length=100)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_edad', models.IntegerField()),
                ('user_sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_texto', models.CharField(max_length=150)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Area')),
                ('encuesta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Encuesta')),
            ],
        ),
        migrations.AddField(
            model_name='carrera_institucion',
            name='institucion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Institucion'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='area_id',
            field=models.ManyToManyField(through='orientacion.Carrera_Area', to='orientacion.Area'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='institucion',
            field=models.ManyToManyField(through='orientacion.Carrera_Institucion', to='orientacion.Institucion'),
        ),
    ]
