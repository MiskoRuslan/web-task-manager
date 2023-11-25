from django.test import TestCase
from django.contrib.auth import get_user_model
from web_service.forms import (
    PositionForm,
    TaskTypeForm,
    TaskSearchForm,
    WorkerSearchForm
)


class WebServiceFormsTestCase(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='adminpassword',
        )

    def test_position_form_valid_data(self):
        form_data = {"name": "Engineering"}
        form = PositionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_type_form_valid_data(self):
        form_data = {"name": "Development"}
        form = TaskTypeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_search_form_valid_data(self):
        form_data = {"name": "Search Query"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_search_form_valid_data(self):
        form_data = {"username": "Search Query"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
