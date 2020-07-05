import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Task create form for user
    """
    class Meta:
        model = Task
        fields = ['task_title', 'description', 'date_required']
