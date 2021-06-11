from django.db import models


# Create your models here.
class customerBooking(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)
    noOfSeats = models.IntegerField()
    cost = models.IntegerField()
    movie = models.CharField(max_length=1000)


class priceMovies(models.Model):
    name = models.CharField(max_length=200)
    ids = models.IntegerField()
    price = models.BigIntegerField()
