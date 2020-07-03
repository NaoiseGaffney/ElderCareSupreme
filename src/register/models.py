from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserRole(models.Model):
    role = models.CharField(max_length=10, blank=Flase, null=False, unique=True)
    icon = models.CharField(null=False, unique=True)

class UserProfile(models.Model):
    user_name = models.OneToOneField(User)
    city = models.CharField(max_length=60, blank=False, null=False)
    post_code = models.CharField(max_length=60, blank=False, null=False)
    phone_number = PhoneNumberField()
    role = models.ForeignKey(UserRole)