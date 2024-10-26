from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)


class Register(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)