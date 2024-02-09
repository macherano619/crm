from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    celular = models.CharField(max_length=10, blank=False, null=False)
    cedula = models.CharField(max_length=10, blank=False, null=False)
    ciudad = models.CharField(max_length=50, blank=False, null=False,default= 'Quito')


class Imagen(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    nombre = models.ImageField(upload_to="media/")
    detalle_cliente = models.ForeignKey('DetalleCliente', on_delete=models.CASCADE)

   

class DetalleCliente(models.Model):
    id_detalle_cliente = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=50)
    fecha_f = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    comentario = models.CharField(max_length=700)
    programa = models.CharField(max_length=500)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    

    

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=150)
    comentario = models.CharField(max_length=500)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    clave = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)
    grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)
