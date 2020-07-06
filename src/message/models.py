from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from task.models import Task


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Anonymouse")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=False, null=False)
    message = models.CharField(max_length=300, blank=False, null=False)
    date_created = models.DateField(auto_now_add=False, default=timezone.now)
    date_edited = models.DateField(auto_now_add=timezone.now)

    def __str__(self):
        return f'{self.user} + {self.task}'
