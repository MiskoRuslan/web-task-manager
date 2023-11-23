from django.urls import path

from web_service.views import (
    home_page_view,
    PositionsListView,
    TasksTypeListView,
    PositionsCreateView,
    PositionsUpdateView,
    PositionsDeleteView,
    TasksTypeCreateView,
    TasksTypeUpdateView,
    TasksTypeDeleteView,
    WorkersListView,
    WorkerCreateView,
    WorkersDetailView,
    TasksListView,
    TaskCreateView,
    TaskUpdateView,
    WorkerUpdateView,
    WorkerDeleteView,
    WorkerProfileView,
    my_task_list_view,
)

app_name = "web_service"

urlpatterns = [
    path("", home_page_view, name="home-page"),
    path("positions-list/", PositionsListView.as_view(), name="positions-list"),
    path("positions-list/create/", PositionsCreateView.as_view(), name="positions-create"),
    path("positions-list/<int:pk>/update/", PositionsUpdateView.as_view(), name="positions-update"),
    path("positions-list/<int:pk>/delete/", PositionsDeleteView.as_view(), name="positions-delete"),
    path("tasks-type-list/", TasksTypeListView.as_view(), name="tasks-type-list"),
    path("tasks-type-list/create/", TasksTypeCreateView.as_view(), name="tasks-type-create"),
    path("tasks-type-list/<int:pk>/update/", TasksTypeUpdateView.as_view(), name="tasks-type-update"),
    path("tasks-type-list/<int:pk>/delete/", TasksTypeDeleteView.as_view(), name="tasks-type-delete"),
    path("workers-list/", WorkersListView.as_view(), name="workers-list"),
    path("worker-list/<int:pk>/detail", WorkersDetailView.as_view(), name="worker-detail"),
    path("worker-create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker-list/<int:pk>/detail/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("worker-list/<int:pk>/detail/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("tasks-list/", TasksListView.as_view(), name="tasks-list"),
    path("tasks-list/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("my-profile/", WorkerProfileView.as_view(), name="worker-profile"),
    path('my-tasks/', my_task_list_view, name='my-task-list'),
]
