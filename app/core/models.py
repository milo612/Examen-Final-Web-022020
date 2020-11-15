from django.db import models

class Computadora(models.Model):
    desc = models.CharField(max_length=100)
    precio = models.CharField(max_length=15)
    class Meta:
        db_table = "computadora"