from django.db import models
class flightbookdata(models.Model):
    passenger=models.CharField(max_length=50)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    date=models.DateTimeField()
    seat=models.IntegerField()
