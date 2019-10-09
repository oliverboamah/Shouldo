# Django imports
from django.urls import path

# My App imports
from tasks.views import task_views

app_name = 'tasks'

urlpatterns = [
    path(route='', view=task_views.get_all_tasks, name='index'),
    path(route='tasks/create', view=task_views.create_task, name='create'),
    path(route='tasks/task-detail/<int:id>', view=task_views.get_task, name='detail'),
    path(route='tasks/update/<int:id>', view=task_views.update_task, name='update'),

    # json get request
    path(route='tasks/get-task-json/<int:id>', view=task_views.get_task_json)
]
