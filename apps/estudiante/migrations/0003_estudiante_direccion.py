# Generated by Django 2.0.3 on 2018-03-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_estudiante_carrera_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
