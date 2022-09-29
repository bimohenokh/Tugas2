from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_todolist", null=True)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.TextField()
    