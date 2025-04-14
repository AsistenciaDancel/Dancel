from django.db import models


class Materia(models.Model):
    nombre= models.CharField(max_length=50)
    profesor= models.CharField(max_length=20)

    def __str__(self):
        return self.nombre  

class Libro(models.Model):
    autor= models.CharField(max_length=40)
    archivo = models.FileField(upload_to='libros/', null=True, blank=True)
    modelo_parcial = models.FileField(upload_to='modelo/', null=True, blank=True)
    materia= models.ForeignKey(Materia, on_delete=models.CASCADE)

class Progreso(models.Model):
    fecha_parcial1= models.DateField(null=True, blank=True)
    fecha_parcial2= models.DateField()
    fecha_tp= models.DateField(null=True, blank=True)
    fecha_final= models.DateField()
    fecha_final2= models.DateField(null=True, blank=True)
    materia= models.ForeignKey(Materia, on_delete=models.CASCADE)



