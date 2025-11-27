# habits/models.py
from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    completed_today = models.BooleanField(default=False)
    frequency = models.CharField(max_length=10)
    streak = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
