from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# DEFAULT_USER_ID = 2

class Component(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lot_number = models.CharField(max_length=200, unique=True)
    expiration_date = models.DateField()
    crt_part_number = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)