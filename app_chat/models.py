from django.db import models
from django.contrib.auth.models import User

class Conversacion(models.Model):
    participantes = models.ManyToManyField(User, related_name='conversaciones')

    def __str__(self):
        return "{}".format(self.pk)

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, related_name='mensajes', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, related_name='mensajes', on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.autor.username, self.fecha_hora)
