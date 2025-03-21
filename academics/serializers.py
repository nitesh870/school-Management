from rest_framework import serializers
from .models import Class, Subject ,Exam,Marks,Period,TimeTable,Attendance,ReportCard

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

from rest_framework import serializers
from .models import TimeTable, Period

class TimeTableSerializer(serializers.ModelSerializer):
    periods = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Period.objects.all()
    )

    class Meta:
        model = TimeTable
        fields = '__all__'




class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = '__all__'