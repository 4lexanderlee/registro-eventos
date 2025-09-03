from django.db import models
from django.utils import timezone

class Evento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    fecha = models.DateField(verbose_name="Fecha del Evento")
    ubicacion = models.CharField(max_length=255, verbose_name="Ubicación")
    organizador = models.CharField(max_length=100, verbose_name="Organizador")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha']
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"