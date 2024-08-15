from django.db import models

# Create your models here.
# Does the curia need a parish? Yes? for specification
class Curia(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Nigeria")
    parish = models.CharField(max_length=100)
    spiritual_director = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "_curia"


class Announcement(models.Model):
    curia = models.ForeignKey(Curia, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/curia/')

    def __str__(self):
        return self.name[:20]