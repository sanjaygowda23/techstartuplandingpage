from django.db import models

# Create your models here.


class database(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    service = models.CharField(max_length=20, null=True)
    message = models.CharField(max_length=200)
