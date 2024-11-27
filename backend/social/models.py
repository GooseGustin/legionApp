from django.db import models
from accounts.models import Legionary

# Create your models here.
'''
Question: 
    - content
    - legionary
    - flags

Answer: 
    - content
    - legionary
    - question
    - upvote
    - downvote
    - flags

Post: 
    - title
    - content
    - image
    - legionary
    - upvote
    - downvote
    - flags

'''

class Question(models.Model):
    content = models.TextField()
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="question")
    date = models.DateTimeField(auto_now_add=True)
    flags = models.IntegerField()

class Answer(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    flags = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="images/posts")
    date = models.DateTimeField(auto_now_add=True)
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="answer")
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    flags = models.IntegerField()