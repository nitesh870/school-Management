from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer

#  Get All Teachers & Create New Teacher
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Get, Update, Delete Specific Teacher
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
