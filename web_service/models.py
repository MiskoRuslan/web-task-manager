from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from web_task_manager.settings import AUTH_USER_MODEL


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, default="Intern")

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.username} -> {self.position}"

    def get_absolute_url(self):
        return reverse("web_service:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent", 1),
        ("High", 2),
        ("Medium", 3),
        ("Low", 4),
        ("Not time-sensitive", 5),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(AUTH_USER_MODEL)

    def __str__(self):
        return self.name
