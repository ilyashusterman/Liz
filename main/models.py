from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Trip(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    stops = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trip_images',
                              default='media/default.png')

    def __str__(self):
        return self.name
