from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)