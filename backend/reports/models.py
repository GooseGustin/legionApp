from django.db import models
from praesidium.models import Praesidium

# Create your models here.
class Report(models.Model):
    praesidium = models.ForeignKey(Praesidium, on_delete=models.CASCADE)
    submission_date = models.DateField()
    last_submission_date = models.DateField()
    report_number = models.IntegerField()
    report_period = models.DurationField()
    last_curia_visit_date = models.DateField()
    last_curia_visitors = models.JSONField(default=list)
    officers_curia_attendance = models.JSONField(default=dict)
    officers_meeting_attendance = models.JSONField(default=dict)
    extension_plans = models.TextField()
    problems = models.TextField()
    remarks = models.TextField()
    no_meetings_expected = models.IntegerField()
    no_meetings_held = models.IntegerField()
    avg_attendance = models.IntegerField()
    poor_attendance_reason = models.TextField()

class FunctionAttendance(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField()
    current_year_attendance = models.IntegerField()
    previous_year_attandance = models.IntegerField()

class MembershipDetails(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    senior_praesidia = models.IntegerField()
    junior_praesidia = models.IntegerField()
    active_members = models.IntegerField()
    probationary_members = models.IntegerField()
    auxiliary_members = models.IntegerField()
    adjutorian_members = models.IntegerField()
    praetorian_members = models.IntegerField()

class Achievement(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    no_recruited = models.IntegerField()
    no_baptized = models.IntegerField()
    no_confirmed = models.IntegerField()
    no_first_communicants = models.IntegerField()
    others = models.JSONField(default=dict)
