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
        fields = ['id', 'start_time', 'end_time', 'day_of_week', 'subject', 'teacher']

from rest_framework import serializers
from .models import TimeTable, Period

class TimeTableSerializer(serializers.ModelSerializer):
    periods = PeriodSerializer(many=True)  # Nested serializer allow karna hoga

    class Meta:
        model = TimeTable
        fields = '__all__'

    def create(self, validated_data):
        periods_data = validated_data.pop('periods')
        timetable = TimeTable.objects.create(**validated_data)
        for period_data in periods_data:
            Period.objects.create(timetable=timetable, **period_data)
        return timetable





class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = '__all__'