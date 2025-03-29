from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Class, Subject,Exam, Marks
from .serializers import ClassSerializer, SubjectSerializer,ExamSerializer, MarksSerializer

#  Class API
class ClassListCreateView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    def create(self, request, *args, **kwargs):
        # Check if request data is a list (multiple objects)
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

#  Subject API
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
#....

# ✅ Exam API
class ExamListCreateView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

# ✅ Marks API
class MarksListCreateView(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MarksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer


from .models import Period, TimeTable
from .serializers import PeriodSerializer, TimeTableSerializer

# ✅ Period API
class PeriodListCreateView(generics.ListCreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
   
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# ✅ Period Detail API (Retrieve, Update, Delete)
class PeriodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

# ✅ TimeTable API
# ✅ TimeTable List & Create API
class TimeTableListCreateView(generics.ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# ✅ TimeTable Detail API (Retrieve, Update, Delete)
class TimeTableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

from .models import Attendance
from .serializers import AttendanceSerializer

# ✅ Attendance Create aur List API
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# ✅ Attendance Detail (Retrieve, Update, Delete) API
class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

from .models import ReportCard
from .serializers import ReportCardSerializer

# ✅ Report Card List & Create API
class ReportCardListCreateView(generics.ListCreateAPIView):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer
  
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # Check if request contains a list (Bulk Create)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# ✅ Report Card Detail API (Retrieve, Update, Delete)
class ReportCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer