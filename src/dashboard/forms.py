from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    User profile form, that takes models from UserProfile model
    """
    class Meta:
        model = UserProfile
        fields = ['role', 'city', 'post_code', 'phone_number']
