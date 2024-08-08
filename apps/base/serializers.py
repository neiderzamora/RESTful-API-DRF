from rest_framework import serializers
from .models import *

class TreatmentMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment_Medicine
        fields = '__all__'
        read_only_fields = 'id'

class DiseaseTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease_Treatment
        fields = '__all__'
        read_only_fields = 'id'