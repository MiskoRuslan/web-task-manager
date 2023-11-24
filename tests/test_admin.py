from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from web_service.models import TaskType, Position, Worker, Task


class AdminTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_superuser(
            username='admin',
            password='adminpassword',
        )
        self.client.force_login(self.user)

        self.task_type = TaskType.objects.create(name='Test Type')
        self.position = Position.objects.create(name='Test Position')
        self.worker = Worker.objects.create(username='test_worker', position=self.position)
        self.task = Task.objects.create(
            name='Test Task',
            description='Test Description',
            deadline='2023-12-31',
            is_completed=False,
            priority='Urgent',
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)

    def test_task_type_admin(self):
        response = self.client.get(reverse('admin:web_service_tasktype_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task_type.name)

    def test_position_admin(self):
        response = self.client.get(reverse('admin:web_service_position_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.position.name)

    def test_worker_admin(self):
        response = self.client.get(reverse('admin:web_service_worker_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.worker.username)

    def test_task_admin(self):
        response = self.client.get(reverse('admin:web_service_task_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)
