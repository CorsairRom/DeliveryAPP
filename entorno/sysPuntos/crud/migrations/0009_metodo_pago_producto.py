# Generated by Django 4.0.6 on 2022-11-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_alter_promocion_id_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='metodo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pago', models.CharField(max_length=50, null=True, verbose_name='Nombre Metodo')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_producto', models.CharField(max_length=50, null=True, verbose_name='Nombre producto')),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
