# Generated by Django 2.0.3 on 2018-03-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especialidad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidad',
            name='carrera',
        ),
    ]
