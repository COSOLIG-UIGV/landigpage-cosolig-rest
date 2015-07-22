from django.db import models
from django.utils import timezone
from django.db import models

class Post(models.Model):
    fecha_publicacion = models.DateTimeField(default=timezone.now())
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __unicode__(self):
        return self.titulo
# Create your models here.
