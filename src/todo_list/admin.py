from django.contrib import admin

from todo_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "date", "deadline", "is_done")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
