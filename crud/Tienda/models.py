from django.db import models
from django.contrib.auth.models import User

class Comic(models.Model):
    comic = models.CharField(max_length=100)
    tomo =  models.CharField(max_length=80)
    titulo = models.CharField(max_length=100)
    info = models.TextField(max_length=1200)
    precio = models.FloatField()
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    publicado_el = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.titulo}"


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    instagram = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="profiles", null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")

def __str__(self):
        return f"{self.email}"