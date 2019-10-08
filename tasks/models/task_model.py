# Django imports
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    detail = models.TextField(blank=False)
    due_date = models.DateField(blank=False)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
