from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TagForm, TaskForm
from todo_list.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/page_task.html"
    queryset = Task.objects.prefetch_related("tags")

    def get_queryset(self):
        task_id = self.request.GET.get("done") or self.request.GET.get("not-done")
        if task_id:
            is_done = "done" in self.request.GET
            Task.objects.filter(id=task_id).update(is_done=is_done)
        return Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_update.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_update.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "tag/tag_update.html"
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "tag/tag_update.html"
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")
