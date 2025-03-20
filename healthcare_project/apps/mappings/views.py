from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingDetailSerializer
from apps.doctors.models import Doctor

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PatientDoctorMappingDetailSerializer
        return PatientDoctorMappingSerializer
    
    @action(detail=False, methods=['get'], url_path=r'patient/(?P<patient_id>\d+)')
    def get_doctors_for_patient(self, request, patient_id=None):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingDetailSerializer(mappings, many=True)
        return Response(serializer.data)