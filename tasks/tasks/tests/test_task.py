import pytest
from main.models import Task
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_task_create(create_task):
    task = create_task(name="task1")
    assert task.name == "task1"
    assert task.status == "N"
    assert len(Task.objects.all()) == 1


@pytest.mark.django_db
def test_creating_task(client):
    res = client.get(reverse("task-list"))
    assert res.status_code == 200


@pytest.mark.django_db
def test_update_task(create_task, client):
    task = create_task(name="task1")
    res = client.put(reverse("task-detail", args=[task.id]), {"name": "task2"})
    assert res.status_code == 200
    task.refresh_from_db()
    assert task.name == "task2"


@pytest.mark.django_db
def test_delete_task(create_task, client):
    task = create_task(name="task1")
    res = client.delete(reverse("task-detail", args=[task.id]))
    assert res.status_code == 204
    assert len(Task.objects.all()) == 0


@pytest.mark.django_db
def test_filtering_by_name(create_task, client):
    create_task(name="task1")
    create_task(name="task2")
    res = client.get(reverse("task-list"), {"search": "task1"})
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["name"] == "task1"


@pytest.mark.django_db
def test_filtering_by_description(create_task, client):
    create_task(name="task1", description="description1")
    create_task(name="task2", description="description2")
    res = client.get(reverse("task-list"), {"search": "description1"})
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["description"] == "description1"


@pytest.mark.django_db
def test_filtering_by_status(create_task, client):
    create_task(name="task1", status="C")
    create_task(name="task2", status="N")
    res = client.get(reverse("task-list"), {"status": "C"})
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["status"] == "C"


@pytest.mark.django_db
def test_auth_req():
    client = APIClient()
    res = client.get(reverse("task-list"))
    assert res.status_code == 401
