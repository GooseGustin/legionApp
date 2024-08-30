from django.db import models
from praesidium.models import Praesidium

# Create your models here.
class Report(models.Model):
    # Once a legionary/praesidium pays to create a report, a blank report is created for the managers to fill in before the edit_deadline date
    # won't there be a create report button? won't that also create new blank reports? 
    # How about just a form instead? Fill the form to create a report. it is saved and you come back often to update it before the praesidium report deadline 
    praesidium = models.ForeignKey(Praesidium, on_delete=models.CASCADE)
    submission_date = models.DateField(null=True, blank=True)
    last_submission_date = models.DateField(null=True, blank=True)
    report_number = models.IntegerField(default=0)
    report_period = models.IntegerField(default=0) # days
    last_curia_visit_date = models.DateField(null=True, blank=True)
    last_curia_visitors = models.JSONField(default=list)
    officers_curia_attendance = models.JSONField(default=dict)
    officers_meeting_attendance = models.JSONField(default=dict)
    extension_plans = models.TextField(null=True, blank=True)
    problems = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    no_meetings_expected = models.IntegerField(default=0)
    no_meetings_held = models.IntegerField(default=0)
    avg_attendance = models.IntegerField(default=0)
    poor_attendance_reason = models.TextField(null=True, blank=True)

class FunctionAttendance(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField()
    current_year_attendance = models.IntegerField(default=0)
    previous_year_attendance = models.IntegerField(default=0)

class MembershipDetails(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    senior_praesidia = models.IntegerField(default=0)
    junior_praesidia = models.IntegerField(default=0)
    active_members = models.IntegerField(default=0)
    probationary_members = models.IntegerField(default=0)
    auxiliary_members = models.IntegerField(default=0)
    adjutorian_members = models.IntegerField(null=True, blank=True)
    praetorian_members = models.IntegerField(null=True, blank=True)

class Achievement(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    no_recruited = models.IntegerField(null=True, blank=True)
    no_baptized = models.IntegerField(null=True, blank=True)
    no_confirmed = models.IntegerField(null=True, blank=True)
    no_first_communicants = models.IntegerField(null=True, blank=True)
    others = models.JSONField(default=dict, null=True, blank=True)
