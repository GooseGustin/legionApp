from django.db import models
from meetings.models import Meeting
from reports.models import Report

# Create your models here.
class Expenses(models.Model):
    extension = models.FloatField(default=0)
    remittance = models.FloatField(default=0)
    stationery = models.FloatField(default=0)
    altar = models.FloatField(default=0)
    bouquet = models.FloatField(default=0)
    others = models.JSONField(default=dict)

class AcctStatement(models.Model):
    acf = models.FloatField()
    sbc = models.FloatField()
    balance = models.FloatField()
    expenses = models.OneToOneField(Expenses, on_delete=models.CASCADE)

class AcctAnnouncement(models.Model):
    sbc = models.FloatField()
    collection_1 = models.FloatField()
    collection_2 = models.FloatField()

class FinancialRecord(models.Model):
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE)
    acct_statement = models.OneToOneField(AcctStatement, on_delete=models.CASCADE)
    acct_announcement = models.OneToOneField(AcctAnnouncement, on_delete=models.CASCADE)
    
class FinancialSummary(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    abf = models.FloatField()
    sbc = models.JSONField(default=dict)
    expenses = models.JSONField(default=dict)
    report_production = models.FloatField()
