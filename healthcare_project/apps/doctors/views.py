from rest_framework import viewsets, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Ensure users can only see their own doctors
        return Doctor.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically associate the doctor with the current user
        serializer.save(user=self.request.user)