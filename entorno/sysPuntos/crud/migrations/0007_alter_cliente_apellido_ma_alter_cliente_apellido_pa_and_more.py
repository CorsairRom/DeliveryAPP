# Generated by Django 4.0.6 on 2022-11-16 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_alter_promocion_fecha_ini'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido_ma',
            field=models.CharField(max_length=30, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido_pa',
            field=models.CharField(max_length=30, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion_cli',
            field=models.CharField(max_length=50, verbose_name='Direccion Principal'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut_cliente',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='cliente_dir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.cliente', verbose_name='Direccion cliente'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='nombre_dir',
            field=models.CharField(max_length=50, verbose_name='Nombre direcion'),
        ),
        migrations.AlterField(
            model_name='local',
            name='direccion_local',
            field=models.CharField(max_length=200, null=True, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='local',
            name='nombre_local',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='descripcion_promo',
            field=models.CharField(max_length=50, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha_fin',
            field=models.DateField(null=True, verbose_name='fecha fin'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='nombre_promo',
            field=models.CharField(max_length=50, null=True, verbose_name='nombre'),
        ),
    ]
