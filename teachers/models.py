from django.db import models

# Create your models here.
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    # subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE, related_name='assigned_teachers')
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
