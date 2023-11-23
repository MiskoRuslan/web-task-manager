from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from django.views import generic

from web_service.models import Position, TaskType


def home_page_view(request: HttpRequest) -> HttpResponse:
    return render(request, "service_parts/home.html")


class PositionsListView(generic.ListView):
    model = Position
    template_name = "service_parts/positions_list.html"
    context_object_name = "positions_list"


class TasksTypeListView(generic.ListView):
    model = TaskType
    template_name = "service_parts/tasks_type_list.html"
    context_object_name = "tasks_type_list"
