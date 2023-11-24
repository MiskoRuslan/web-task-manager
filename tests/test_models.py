from datetime import date
from django.test import TestCase
from web_service.models import TaskType, Worker, Task, Position


class TaskTypeModelTest(TestCase):
    def test_str_method(self):
        task_type = TaskType.objects.create(name="Test Task Type")
        self.assertEqual(str(task_type), "Test Task Type")


class TaskModelTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.worker = Worker.objects.create(username="testuser")

    def test_str_method(self):
        task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline=date.today(),
            priority="Urgent",
            task_type=self.task_type,
        )
        self.assertEqual(str(task), "Test Task")


class WorkerModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Test Position")

    def test_str_method(self):
        worker = Worker.objects.create(username="testuser", position=self.position)
        self.assertEqual(str(worker), "testuser -> Test Position")

    def test_get_absolute_url(self):
        worker = Worker.objects.create(username="testuser", position=self.position)
        url = worker.get_absolute_url()
        self.assertEqual(url, f"/worker-list/{worker.pk}/detail/")


class PositionModelTest(TestCase):
    def test_str_method(self):
        position = Position.objects.create(name="Test Position")
        self.assertEqual(str(position), "Test Position")
