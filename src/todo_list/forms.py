from django import forms

from todo_list.models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
