from django.db import models

# Create your models here.

class Users(models.Model):
    pass


class Register(models.Model):
    name = models.CharField(max_length=122)
    emailid = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    emailid = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    ocupation = models.CharField(max_length=122)
    details = models.TextField("")
    date = models.DateField("")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=122)
    emailid = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    details = models.TextField("")
    date = models.DateField("")

    def __str__(self):
        return self.name
