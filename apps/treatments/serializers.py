from rest_framework import serializers
from .models import Treatment
from apps.medicines.serializers import MedicineSerializer

class TreatmentSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(many=True, read_only=True)
    class Meta:
        model = Treatment
        fields = '__all__'
        read_only_fields = ['id']
        