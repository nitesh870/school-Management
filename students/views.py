from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Student,Enrollment
from .serializers import StudentSerializer,EnrollmentSerializer

#  Get All Students & Create New Student
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#  Get, Update, Delete Specific Student
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    


# ✅ Enrollment List & Create API
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# ✅ Enrollment Detail API (Retrieve, Update, Delete)
class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
