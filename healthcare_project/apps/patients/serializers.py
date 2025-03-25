from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 
            'gender', 'blood_group', 'phone_number', 
            'address', 'medical_history'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']