from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer

#  Get All Teachers & Create New Teacher
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#  Get, Update, Delete Specific Teacher
# Get, Update, Delete Specific Teacher
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
