from django.db import models

# Create your models here.

class Artist(models.Model):
    """Name of a musical artist"""
    name = models.CharField(max_length=200)

      
    def __str__(self):
        """return a string reppresentation of the model"""
        return self.name


class Song(models.Model):
    """Song names by musical artists"""
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        """return a string reppresentation of the model"""
        return self.name
