from django.db import models

class Destination(models.Model):
        #id: str
        name = models.CharField(max_length=100)
        img = models.ImageField(upload_to='pics')
        #img = models.CharField(max_length=100)
        desc = models.CharField(max_length=100)
        price = models.IntegerField()
        offer = models.BooleanField(default=False)
