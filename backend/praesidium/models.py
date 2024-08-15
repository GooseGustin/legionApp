from django.db import models
from curia.models import Curia
from accounts.models import Legionary

# Create your models here.
class Praesidium(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Nigeria")
    parish = models.CharField(max_length=50)
    curia = models.ForeignKey(Curia, on_delete=models.CASCADE)
    iden = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    meeting_time = models.CharField(max_length=100)
    inaug_date = models.DateField()
    president = models.CharField(max_length=100)
    pres_app_date = models.DateField()
    vice_president = models.CharField(max_length=100)
    vp_app_date = models.DateField()
    secretary = models.CharField(max_length=100)
    sec_app_date = models.DateField()
    treasurer = models.CharField(max_length=100)
    tres_app_date = models.DateField()
    managers = models.ManyToManyField(Legionary)

    def __str__(self):
        return self.name + '_praesidium'

class Reminder(models.Model):
    praesidium = models.ForeignKey(
        Praesidium, on_delete=models.CASCADE
    )
    content = models.TextField()
    deadline = models.DateField()
