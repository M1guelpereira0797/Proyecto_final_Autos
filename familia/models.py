from django.db import models
class familia(models.Model):
    nombre =models.CharField(max_length=100)
    
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.direccion},{self.numero_pasaporte}, {self.id}"

class Vehiculos(models.Model):
    nombre_vehiculo= models.CharField(max_length=100)
    
    marca_vehiculo = models.CharField(max_length=200)
    numero_de_vehiculo = models.IntegerField()
    def __str__(self):
      return f"{self.nombre_vehiculo}, {self.marca_vehiculo},{self.numero_de_vehiculo}"

class Equipo_de_futbol(models.Model):
    nombre_equipo= models.CharField(max_length=100)
    
    marca_deportiva = models.CharField(max_length=200)
    numero_de_jugador_favorito = models.IntegerField()
    def __str__(self):
      return f"{self.nombre_equipo}, {self.marca_deportiva},{self.numero_de_jugador_favorito}"