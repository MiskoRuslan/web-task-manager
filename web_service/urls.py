from django.urls import path

from web_service.views import home_page_view, PositionsListView, TasksTypeListView

app_name = "web_service"

urlpatterns = [
    path("", home_page_view, name="home-page"),
    path("positions-list/", PositionsListView.as_view(), name="positions-list"),
    path("tasks-type-list/", TasksTypeListView.as_view(), name="tasks-type-list"),
]
