from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TaskCategory(models.Model):
    category = models.CharField(max_length=30, blank=False, null=False)
    icon = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.category

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)
    aider = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='aider')
    task_title = models.CharField(max_length=30, blank=False, null=False, verbose_name='title')
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, blank=False, null=True)
    description = models.TextField(max_length=300, blank=False, null=False)
    is_done = models.BooleanField(blank=False, null=False, default=False)
    date_created = models.DateField(auto_now_add=False, default=timezone.now)
    date_required = models.DateField(auto_now_add=False, default=timezone.now)

    def get_aider_url(self):
        return reverse('aider', kwargs={'id': self.id})
    
    def get_aider_api_url(self):
        return reverse('aider_api', kwargs={'id': self.id})

    def __str__(self):
        return self.task_title
