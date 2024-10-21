from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)