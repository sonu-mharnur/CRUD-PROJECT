from django.db import models

# Create your models here.

class UserData(models.Model):
    fullname = models.CharField('full name',max_length=100)
    emailid = models.EmailField('emailid',max_length=100)
    contact = models.IntegerField('contanct number')
    address = models.CharField('address',max_length=100)
    username = models.CharField('username',max_length=20)
    password = models.CharField('password',max_length=20)
