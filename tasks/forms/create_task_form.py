# Django imports
from django import forms

# My App imports
from tasks.models.task_model import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'detail', 'due_date']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title',
                    'class': 'form-control form-control-line'
                }
            ),
            'detail': forms.Textarea(
                attrs={
                    'placeholder': 'Enter detail',
                    'class': 'form-control form-control-line'
                }
            ),
            'due_date': forms.DateInput(
                attrs={
                    'placeholder': 'Schedule date',
                    'class': 'form-control form-control-line',
                    'type': 'date'
                }
            ),
        }
