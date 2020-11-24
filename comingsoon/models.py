from django.db import models

# Create your models here.
class order(models.Model):

    name = models.CharField(max_length=500)
    number = models.IntegerField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    province = models.CharField(max_length=500)
    zipcode = models.IntegerField()
    item = models.CharField(max_length=500)
    quantity = models.CharField(max_length=3)
    method = models.CharField(max_length=100)
    
    


