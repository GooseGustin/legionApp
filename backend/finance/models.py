from django.db import models
from meetings.models import Meeting
from reports.models import Report

# Create your models here.
class Expenses(models.Model):
    extension = models.FloatField()
    remittance = models.FloatField()
    stationery = models.FloatField()
    altar = models.FloatField()
    bouquet = models.FloatField()
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
    abf = models.FloatField()
    sbc = models.JSONField(default=dict)
    expenses = models.JSONField(default=dict)
    report_production = models.FloatField()
