from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    tel = models.CharField(max_length=32)
    belong = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True)
