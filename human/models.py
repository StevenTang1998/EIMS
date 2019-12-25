from django.db import models


class Serving(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    human_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
