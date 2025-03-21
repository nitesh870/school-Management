from django.db import models
from students.models import Student
from teachers.models import Teacher
# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., "10th Grade", "12th Science"
    section = models.CharField(max_length=10, blank=True, null=True)  # e.g., "A", "B"

    def __str__(self):
        return f"{self.name} - {self.section}" if self.section else self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Mathematics", "Physics"
    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.SET_NULL, null=True,related_name='subjects')
    class_assigned = models.ForeignKey("academics.Class", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.class_assigned})"

# ab next

class Exam(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Mid-Term", "Final Exam"
    date = models.DateField()

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    subject = models.ForeignKey("academics.Subject", on_delete=models.CASCADE)
    exam = models.ForeignKey("academics.Exam", on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField(default=100)

    def __str__(self):
        return f"{self.student} - {self.subject} ({self.marks_obtained}/{self.total_marks})"

class Period(models.Model):
    class_assigned = models.ForeignKey("academics.Class", on_delete=models.CASCADE)
    subject = models.ForeignKey("academics.Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(
        max_length=10,
        choices=[("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"),
                 ("Thursday", "Thursday"), ("Friday", "Friday"), ("Saturday", "Saturday")]
    )

    def __str__(self):
        return f"{self.class_assigned} - {self.subject} ({self.start_time} - {self.end_time})"


# class TimeTable(models.Model):
#     class_assigned = models.ForeignKey("academics.Class", on_delete=models.CASCADE)
#     periods = models.ManyToManyField("academics.Period")

#     def __str__(self):
#         return f"TimeTable for {self.class_assigned}"

# ab attendance

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10, 
        choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

    class Meta:
        unique_together = ('student', 'date')  # Ek student ek din me ek baar mark ho


# ab next TimeTable



class TimeTable(models.Model):
    class_assigned = models.ForeignKey("academics.Class", on_delete=models.CASCADE)
    periods = models.ManyToManyField("academics.Period", related_name="timetables")

    def __str__(self):
        return f"TimeTable for {self.class_assigned}"

# from django.db import models
# from academics.models import Subject, Teacher

# class Period(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.subject.name} ({self.start_time} - {self.end_time})"

# from django.db import models

class ReportCard(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50, choices=[("midterm", "Midterm"), ("final", "Final")])
    total_marks_obtained = models.FloatField()
    percentage = models.FloatField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.exam_type} Report"




