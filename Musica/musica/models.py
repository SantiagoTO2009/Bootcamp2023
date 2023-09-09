from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    duracion = models.DurationField()
    archivo_mp3 = models.FileField(upload_to='canciones/')

    def __str__(self):
        return self.titulo