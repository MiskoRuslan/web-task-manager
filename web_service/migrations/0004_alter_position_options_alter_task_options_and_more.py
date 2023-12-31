# Generated by Django 4.2.7 on 2023-11-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_service", "0003_alter_worker_position"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="position",
            options={"ordering": ("name",)},
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["priority"]},
        ),
        migrations.AlterModelOptions(
            name="tasktype",
            options={"ordering": ("name",)},
        ),
        migrations.AlterModelOptions(
            name="worker",
            options={"ordering": ("position__name",)},
        ),
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
