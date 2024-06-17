from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256, null=True)
    status = models.CharField(
        choices=[("N", "New"), ("P", "Pending"), ("C", "Completed")],
        default="N",
        max_length=1,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords()
