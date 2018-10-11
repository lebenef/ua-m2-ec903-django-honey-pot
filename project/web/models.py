from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)


class Contact(models.Model):
    sujet = models.CharField(max_length=100)
    message = models.TextField()
    envoyeur = models.CharField(max_length=100)
    
    


class Data(models.Model):
    addressip = models.CharField(max_length=100)
    useragent = models.CharField(max_length=100)
    datetime = models.DateField()


