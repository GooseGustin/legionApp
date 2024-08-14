from django.db import models
from django.contrib.auth.models import User
from curia.models import Curia 

# Create your models here.
status_options = {
    'manager':'manager', 'non-manager': 'non-manager'
}

class Legionary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_options)
    curia_managed = models.ForeignKey(
        Curia, on_delete=models.SET_NULL, null=True,
        related_name='managers')

    def isManager(self):
        return self.status == 'manager'
    
    def __str__(self):
        return "Legionary " + self.user.username