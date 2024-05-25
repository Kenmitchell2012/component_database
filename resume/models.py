from django.db import models

# Create your models here.

class Component(models.Model):
    name = models.CharField(max_length=200)
    lot_number = models.CharField(max_length=200, unique=True)
    expiration_date = models.DateField()
    crt_part_number = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)