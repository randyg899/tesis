# Generated by Django 2.0.3 on 2018-03-11 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('perfil_empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilempresa',
            name='empresa_perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa'),
        ),
        migrations.AlterField(
            model_name='perfilempresa',
            name='remuneracion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
