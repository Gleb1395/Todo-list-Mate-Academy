# Generated by Django 4.2 on 2025-01-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
    ]
