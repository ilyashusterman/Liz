from django.db import models


# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    stops = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to='trip_images',
                                default='media/default.png')

    def __str__(self):
        return self.name
