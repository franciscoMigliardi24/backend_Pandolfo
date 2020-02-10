from django.db import models

# Create your models here.

import hashlib
import datetime

class Bloque(models.Model):

    timestamp = models.CharField(max_length=100)
    archivo = models.CharField(max_length=100)
    hashActual = models.CharField(max_length=100)
    hashAnterior = models.CharField(max_length=100)

    def __str__(self):
        return "Bloque " + str(self.id)

