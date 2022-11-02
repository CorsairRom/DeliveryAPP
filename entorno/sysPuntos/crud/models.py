# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=8)
    dv = models.CharField(max_length=1)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    apellidopa = models.CharField(max_length=50)
    apellidoma = models.CharField(max_length=50)
    id_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='id_direccion')

    class Meta:
        managed = False
        db_table = 'cliente'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'
