from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class UserProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=60, null=True)
    post_code = models.CharField(max_length=60, null=True)
    phone_number = models.BigIntegerField(null=True, validators=[MaxValueValidator(99999999999999),MinValueValidator(100000000)])
    is_aider = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return str(self.user_name)
