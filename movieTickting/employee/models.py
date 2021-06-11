from django.db import models


# Create your models here.
class mainSlide(models.Model):
    movieName = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    trailer = models.CharField(max_length=300)
    image = models.ImageField(upload_to='main-slide')


class newRelease(models.Model):
    movieName = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    trailer = models.CharField(max_length=300)
    price = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    rating = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='new-releases')
