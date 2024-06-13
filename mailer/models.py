# models.py
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Recipient(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
