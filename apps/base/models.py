from django.db import models
from apps.diseases.models import Disease
from apps.treatments.models import Treatment
from apps.medicines.models import Medicine

class Treatment_Medicine(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="treatment_medicine")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name="treatment_medicine")

class Disease_Treatment(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name="disease_treatment")
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="disease_treatment")
