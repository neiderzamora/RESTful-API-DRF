from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'disease', DiseaseViewSet)
router.register(r'medicine', MedicineViewSet)
router.register(r'treatment', TreatmentViewSet)
router.register(r'treatment_medicine', TreatmentMedicineViewSet)

urlpatterns = [
    path("", include(router.urls))
]
