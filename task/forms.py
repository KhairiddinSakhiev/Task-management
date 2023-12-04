from django import forms
from .models import Task


# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=50)  
#     created_at = forms.DateTimeField()
#     due_date = forms.DateField()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', "is_done"]
