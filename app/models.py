from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='título'
    )
    description = models.TextField(
        blank=True,
        verbose_name='descripción'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creación'
    )
    datecomplated = models.DateTimeField(
        null=True,
        verbose_name='Tarea completada'
    )
    important = models.BooleanField(
        default=False,
        verbose_name='¿Importante?'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title + ' by ' + self.user.username