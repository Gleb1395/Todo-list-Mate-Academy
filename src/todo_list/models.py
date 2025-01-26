import datetime

from django.db import models
from faker import Faker


class Task(models.Model):
    content = models.TextField(max_length=100)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tasks', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.content

    @staticmethod
    def create_test_task(count: int) -> None:
        fake = Faker()
        now = datetime.datetime.now().date()
        tag_names = ["Urgent", "Home", "Work", "Shop"]
        tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]

        for _ in range(count):
            task = Task.objects.create(
                content=fake.text(max_nb_chars=50),
                deadline=now + datetime.timedelta(days=fake.random_int(min=1, max=10)),
                is_done=fake.boolean()
            )
            task.tags.set(fake.random_elements(tags, length=fake.random_int(min=1, max=len(tags))))


class Tag(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name
