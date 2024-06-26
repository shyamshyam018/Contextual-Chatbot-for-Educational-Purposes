from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_spent = models.PositiveIntegerField(default=0)  # Store time in seconds

    def __str__(self):
        return self.user.username

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    time_spent = models.PositiveIntegerField()  # Store time in seconds

