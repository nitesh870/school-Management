from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_mandatory = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.date})"


class Holiday(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.date})"
