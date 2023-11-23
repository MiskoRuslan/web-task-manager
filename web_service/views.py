from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import DetailView

from web_service.forms import WorkerCreationForm, TaskForm
from web_service.models import Position, TaskType, Worker, Task


@login_required
def home_page_view(request: HttpRequest) -> HttpResponse:
    return render(request, "service_parts/home.html")


class PositionsListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "service_parts/positions_list.html"
    context_object_name = "positions_list"
    paginate_by = 5


class PositionsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("web_service:positions-list")
    template_name = "service_parts/positions_form.html"


class PositionsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("web_service:positions-list")
    template_name = "service_parts/positions_form.html"


class PositionsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "service_parts/positions_confirm_delete.html"
    success_url = reverse_lazy("web_service:positions-list")


class TasksTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "service_parts/tasks_type_list.html"
    context_object_name = "tasks_type_list"
    paginate_by = 5


class TasksTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("web_service:tasks-type-list")
    template_name = "service_parts/tasks_type_form.html"


class TasksTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("web_service:tasks-type-list")
    template_name = "service_parts/tasks_type_form.html"


class TasksTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "service_parts/tasks_type_confirm_delete.html"
    success_url = reverse_lazy("web_service:tasks-type-list")


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "service_parts/workers_list.html"
    context_object_name = "workers_list"
    paginate_by = 5


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = WorkerCreationForm
    model = Worker
    template_name = "service_parts/worker_form.html"


class WorkersDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "service_parts/worker_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WorkerProfileView(LoginRequiredMixin, View):
    template_name = "service_parts/worker_profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"user": self.request.user})


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = "service_parts/worker_confirm_delete.html"
    success_url = reverse_lazy("web_service:workers-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = WorkerCreationForm
    model = Worker
    template_name = "service_parts/worker_form.html"


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "service_parts/tasks_list.html"
    context_object_name = "tasks_list"
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "service_parts/task_form.html"
    success_url = reverse_lazy("web_service:tasks-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "service_parts/task_form.html"
    success_url = reverse_lazy("web_service:tasks-list")


@login_required
def my_task_list_view(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(assignees=request.user)
    return render(request, "service_parts/my_tasks.html", {"my_tasks": tasks})