from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    detail = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail


