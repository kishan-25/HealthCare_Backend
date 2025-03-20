from rest_framework import serializers
from .models import PatientDoctorMapping
from apps.patients.serializers import PatientSerializer
from apps.doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        
class PatientDoctorMappingDetailSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'