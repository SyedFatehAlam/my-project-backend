from django.db import models
import zoneinfo

# Create your models here.
paris_tz = zoneinfo.ZoneInfo("Europe/Paris")

class Item(models.Model):
    name= models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Login(models.Model):
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add=True)