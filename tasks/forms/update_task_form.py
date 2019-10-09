# Django imports
from django import forms

# My App imports
from tasks.models.task_model import Task


class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'detail', 'due_date']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title',
                    'class': 'form-control form-control-line',
                    'name': 'title',
                    'id': 'title'
                }
            ),
            'detail': forms.Textarea(
                attrs={
                    'placeholder': 'Enter detail',
                    'class': 'form-control form-control-line',
                    'name': 'detail',
                    'id': 'detail'
                }
            ),
            'due_date': forms.DateInput(
                attrs={
                    'placeholder': 'Schedule date',
                    'class': 'form-control form-control-line',
                    'type': 'date',
                    'name': 'due_date',
                    'id': 'due_date'
                }
            ),
        }
