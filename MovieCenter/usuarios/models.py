from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.imagen}'

class DescripcionUsuario(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    bio=models.TextField()

    def __str__(self):
        return f'{self.bio}'