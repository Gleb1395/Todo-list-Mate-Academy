from django.urls import path

from todo_list.views import TaskListView, TaskUpdateView, TaskDeleteView, TagListView, TaskCreateView, TagCreateView, \
    TagUpdateView, TagDeleteView

app_name = "todo_list"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("task-update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("task-delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
    path("tag-list", TagListView.as_view(), name="tag-list"),
    path("tag-create", TagCreateView.as_view(), name="tag-create"),
    path("tag-update/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tag-delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),

]
