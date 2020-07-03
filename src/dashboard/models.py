from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRole(models.Model):
    role = models.CharField(max_length=10, blank=False, null=False, unique=True)
    def __str__(self): 
        return self.role

class UserProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=60)
    post_code = models.CharField(max_length=60,)
    phone_number = models.IntegerField(max_length=12)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)