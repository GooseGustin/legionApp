from django.db import models
from praesidium.models import Praesidium

# Create your models here.
class Meeting(models.Model):
    date = models.DateField()
    praesidium = models.ForeignKey(Praesidium, on_delete=models.CASCADE)
    no_present = models.IntegerField()
    officers_meeting_attendance = models.JSONField(default=list)
    officers_curia_attendance = models.JSONField(default=list)

