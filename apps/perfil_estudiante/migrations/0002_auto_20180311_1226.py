# Generated by Django 2.0.3 on 2018-03-11 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_estudiante_carrera_estudiante'),
        ('perfil_estudiante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilestudiante',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='perfilestudiante',
            name='estudiante_perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estudiante.Estudiante'),
        ),
    ]