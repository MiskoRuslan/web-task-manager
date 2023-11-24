from django.test import TestCase
from django.urls import reverse
from datetime import date
from django.contrib.auth import get_user_model
from web_service.models import Position, TaskType, Worker, Task


class ViewsTest(TestCase):
    def setUp(self):
        test_user = get_user_model()
        self.user = test_user.objects.create_user(username='testuser', password='testpassword')
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="Bug Fixing")
        self.worker = Worker.objects.create(username="test_user", position=self.position)
        self.task = Task.objects.create(
            name="Test Task",
            description="This is a test task",
            deadline=date.today(),
            is_completed=False,
            priority="Medium",
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)
        self.client.login(username='testuser', password='testpassword')

    def test_positions_list_view(self):
        response = self.client.get(reverse('web_service:positions-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_parts/positions_list.html')

    def test_positions_create_view(self):
        response = self.client.get(reverse('web_service:positions-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_parts/positions_form.html')

    def test_worker_detail_view(self):
        response = self.client.get(reverse('web_service:worker-detail', kwargs={'pk': self.worker.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_parts/worker_detail.html')
        self.assertEqual(response.context['object'], self.worker)

    def test_task_detail_view(self):
        response = self.client.get(reverse('web_service:task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_parts/task_detail.html')
        self.assertEqual(response.context['object'], self.task)
