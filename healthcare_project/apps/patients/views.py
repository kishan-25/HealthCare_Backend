from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Ensure users can only see their own patients
        return Patient.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically associate the patient with the current user
        serializer.save(user=self.request.user)