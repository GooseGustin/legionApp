from django.db import models
from meetings.models import Meeting
from praesidium.models import Praesidium
from reports.models import Report 

# Create your models here.
class Work(models.Model):
    type = models.CharField(max_length=50)
    active = models.BooleanField()
    done = models.BooleanField()
    details = models.JSONField(default=dict)
    meeting = models.ForeignKey(
        Meeting, on_delete=models.CASCADE, related_name='works')

    def __str__(self):
        return "Work_" + self.type 

class WorkSummary(models.Model):
    type = models.CharField(max_length=50)
    active = models.BooleanField()
    no_assigned = models.IntegerField()
    no_done = models.IntegerField()
    details = models.JSONField(default=dict)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

class WorkList(models.Model):
    praesidium = models.OneToOneField(Praesidium, on_delete=models.CASCADE)
    details = models.JSONField(default=list)