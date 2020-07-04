from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aider = models.ForeignKey(User, on_delete=modelsCASCADE, blank=True, null=True)
    task_title = models.CharField(max_length=30, blank=Flase, null=False)
    description = models.TextField(max_length=300, blank=False, null=False)
    is_done = models.BooleanField(blank=False, null=False, default=False)
    