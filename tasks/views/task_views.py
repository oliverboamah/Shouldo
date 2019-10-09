# Core Python imports
import json

# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

# My App imports
from tasks.forms.create_task_form import CreateTaskForm
from tasks.forms.update_task_form import UpdateTaskForm
from tasks.models.task_model import Task


# create task
def create_task(request):
    try:
        form = CreateTaskForm(data=request.POST)
        form.is_valid()
        new_task = form.save()
        messages.success(request, f"Task '{new_task.title}' created successfully!")
    except Exception as e:
        messages.error(request, e)

    return redirect('tasks:index')


# delete task
def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
        task.is_deleted = True
        task.save()
        messages.success(request, f"Task '{task.title}' deleted successfully!")
    except Exception as e:
        messages.error(request, e)

    return redirect('tasks:index')


# update task
def update_task(request, id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(pk=id)
            form = UpdateTaskForm(data=request.POST, instance=task)
            form.save()
            messages.success(request, 'Task has been updated successfully!')
        except Exception as e:
            messages.error(request, e)

        return redirect('tasks:index')


# retrieve all tasks
def get_all_tasks(request):
    tasks = Task.objects.filter(is_deleted=False)
    create_task_form = CreateTaskForm()
    update_task_form = UpdateTaskForm()

    context = {
        'tasks': tasks,
        'create_task_form': create_task_form,
        'update_task_form': update_task_form
    }
    return render(request=request, template_name='tasks/index.html', context=context)


# show single task
def get_task(request, id):
    task = Task.objects.filter(pk=id).first()

    context = {
        'task': task
    }
    return render(request=request, template_name='tasks/task-detail.html', context=context)


# get task as json
def get_task_json(request, id):
    task = Task.objects.get(pk=id)
    task_dict = {
        'id': task.id,
        'title': task.title,
        'detail': task.detail,
        'due_date': task.due_date
    }

    return JsonResponse(data=task_dict, safe=True)
