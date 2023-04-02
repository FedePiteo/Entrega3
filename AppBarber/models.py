from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    numero_de_cliente = models.IntegerField()


class Barbero(models.Model):
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    experiencia = models.IntegerField()


class Turno(models.Model):
    numero_turno = models.IntegerField()
    corte = models.CharField(max_length=40)
    fecha = models.DateField()
