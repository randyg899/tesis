# Generated by Django 2.0.3 on 2018-03-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=30)),
                ('remuneracion', models.IntegerField(null=True)),
                ('conocimientos_deseados', models.CharField(max_length=300)),
                ('horario_trabajo', models.CharField(max_length=100)),
                ('telefono_contacto', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
