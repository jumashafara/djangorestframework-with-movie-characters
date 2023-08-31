# import models
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.title
    
class Character(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    first_appearance = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
