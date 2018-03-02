from __future__ import unicode_literals


# Create your models here.
from django.db import models


    
class Owner(models.Model):
    name = models.CharField(max_length=200)

class Cats(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField('birthday')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    ownerid =  models.IntegerField(default=0)


class Dogs(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField('birthday')
    ownerid =  models.IntegerField(default=0)



