# Generated by Django 4.0.6 on 2022-11-16 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_alter_cliente_apellido_ma_alter_cliente_apellido_pa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='id_local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.local'),
        ),
    ]