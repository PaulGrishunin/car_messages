from django.db import models


class Owner(models.Model):
    tel_number = models.IntegerField( unique=True, primary_key=True)
    name = models.CharField( max_length=30)


class Car(models.Model):
    reg_number = models.CharField( max_length=10, unique=True, primary_key=True)
    owners = models.ManyToManyField( Owner)


class Message(models.Model):
    sender = models.ForeignKey( Owner, on_delete=models.CASCADE)
    recipient = models.ForeignKey( Car, on_delete=models.CASCADE)
    text = models.CharField( max_length=255)
    createdAt = models.DateTimeField( auto_now_add=True)
    received = models.BooleanField(default=False)
    read = models.BooleanField(default=False)