# Generated by Django 2.0 on 2018-05-25 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orientacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_valor', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('pregunta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientacion.Pregunta')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]