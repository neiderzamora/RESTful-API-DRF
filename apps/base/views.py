from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from apps.diseases.serializers import DiseaseSerializer
from apps.medicines.serializers import MedicineSerializer
from apps.treatments.serializers import TreatmentSerializer
from .serializers import *

from apps.diseases.models import Disease
from apps.medicines.models import Medicine
from apps.treatments.models import Treatment
from .models import *

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'id']
    search_fields = ['name', 'id']
    ordering_fields = ['name', 'id']
    

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    
    @action(detail=True, methods=['post'])
    def add_medicine(self, request, pk=None):
        treatment = self.get_object()
        medicine_id = request.data.get('medicine_id')
        
        if not medicine_id:
            return Response({'status': 'medicine_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            medicine_model = Medicine.objects.get(pk=medicine_id)
        except Medicine.DoesNotExist:
            return Response({'status': 'medicine not found'}, status=status.HTTP_404_NOT_FOUND)
        
        treatment.medicine.add(medicine_model)
        treatment.save()
        
        serializer = self.get_serializer(treatment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["post"])
    def remove_medicine(self, request, pk=None):
        treatment = self.get_object()
        medicine_id = request.data.get('medicine_id')
        
        if not medicine_id:
            return Response({'status': 'medicine_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            medicine_model = Medicine.objects.get(pk=medicine_id)
        except Medicine.DoesNotExist:
            return Response({'status': 'medicine not found'}, status=status.HTTP_404_NOT_FOUND)
        
        treatment.medicine.remove(medicine_id)
        treatment.save()
        
        serializer = self.get_serializer(treatment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TreatmentMedicineViewSet(viewsets.ModelViewSet):
    queryset = Treatment_Medicine.objects.all()
    serializer_class = TreatmentMedicineSerializer