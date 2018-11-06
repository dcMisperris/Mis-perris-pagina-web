from django.db import models

# Create your models here.

class Perrito(models.Model):
    OPCIONES_ESTADO = (('Rescatado','Rescatado'),('Disponible','Disponible'),('Adoptado','Adoptado'),)
    fotografia = models.ImageField()
    nombre = models.CharField(max_length = 30)
    raza_predominante = models.CharField(max_length = 50)
    descripcion = models.TextField()
    estado = models.CharField(max_length = 15 , choices = OPCIONES_ESTADO,default = 'Rescatado')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPO_USUARIO = ('administrador','administrador','adoptantes','adoptantes')
