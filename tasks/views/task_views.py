# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages

# My App imports
from tasks.models.task_model import Task
from tasks.forms.create_task_form import CreateTaskForm


# retrieve all tasks
def get_all_tasks(request):
    data = {
        'tasks': Task.objects.all(),
        'store_task_form': CreateTaskForm()
    }
    return render(request, 'tasks/index.html', data)


# store task
def create_task(request):
    form = CreateTaskForm(request.POST)

    try:
        form.is_valid()
        new_task = form.save()
        messages.success(request, f"Task '{new_task.title}' created successfully!")
    except Exception as e:
        messages.error(request, e)

    return redirect('tasks:index')
