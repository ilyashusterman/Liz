from django.db import models


# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    stops = models.CharField(max_length=100)

    def __str__(self):
        return self.name
