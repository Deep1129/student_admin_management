# Generated by Django 5.1.6 on 2025-03-08 14:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0006_alter_attendance_teacher"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="subject",
        ),
        migrations.AlterField(
            model_name="attendance",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="teacher",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="erp.teacher",
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="subject",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="erp.subject",
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="subjects",
            field=models.ManyToManyField(blank=True, to="erp.subject"),
        ),
    ]
