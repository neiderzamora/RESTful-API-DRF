from django.db import models
from apps.medicines.models import Medicine

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    medicine = models.ManyToManyField(Medicine, related_name='treatment_medicines')