from django.db import models
from django.contrib.auth.models import User

STATUS_OPTIONS = [
    ('manager', 'Manager'),
    ('non-manager', 'Non-Manager'),
]

class Legionary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_OPTIONS, default='non-manager'
    )
    premium_status = models.BooleanField(default=False)
    premium_status_deadline = models.DateField(null=True)

    def __str__(self):
        return "Legionary_" + self.user.username

    class Meta: 
        verbose_name_plural = 'legionaries'
