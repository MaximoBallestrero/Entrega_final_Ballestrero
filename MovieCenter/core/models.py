from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    pelicula=models.CharField(max_length=40)
    titulo=models.CharField(max_length=80)
    texto=models.TextField()
    fecha=models.DateField()
    poster=models.ImageField()
    autor=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.pelicula} - {self.titulo} - {self.poster} - {self.autor} - {self.fecha}'