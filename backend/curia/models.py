from django.db import models
from accounts.models import Legionary

# Create your models here.
# Does the curia need a parish? Yes? for specification
class Curia(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Nigeria")
    parish = models.CharField(max_length=100)
    spiritual_director = models.CharField(max_length=100)
    iden = models.CharField(max_length=20)
    creator = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="curia_created")
    managers = models.ManyToManyField(Legionary)
    management_requests = models.ManyToManyField(Legionary, related_name="curia_management_requests")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "_curia"
    
    class Meta: 
        verbose_name_plural = 'curiae'


class Announcement(models.Model):
    curia = models.ForeignKey(Curia, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/curia/')

    def __str__(self):
        return self.title[:20]