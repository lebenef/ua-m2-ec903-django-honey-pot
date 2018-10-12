from django.db import models
from django import forms
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
      
        return self.username


class Contact(models.Model):
    sujet = models.CharField(max_length=100)
    message = models.TextField()
    envoyeur = models.CharField(max_length=100)
    
    
    def __str__(self):

        return self.sujet

    
    


class Data(models.Model):
    addressip = models.CharField(max_length=100)
    useragent = models.CharField(max_length=100)
    datetime = models.DateField()

    def __str__(self):

        return self.addressip



