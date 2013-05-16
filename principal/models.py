from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre 		= models.CharField(max_length=100) 
	#para que no sea requerido models.IntegerField(required=false)
	cantidad	= models.IntegerField()
	precio		= models.FloatField()