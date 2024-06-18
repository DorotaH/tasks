import pytest
from main.models import Task
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

@pytest.fixture
def create_task():
    def _create_task(**kwargs):
        return Task.objects.create(**kwargs)
    return _create_task

@pytest.fixture
def client():
    user = get_user_model().objects.create_user(username='testuser', password='testpassword')
    apiclient = APIClient()
    apiclient.force_authenticate(user=user)
    return apiclient