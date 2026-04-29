from fastapi.testclient import TestClient
from src.main import *

client = TestClient(app)


def setup_function():
    tasks.clear()


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome Donatello!"
    }


def test_add_task():
    response = client.post(
        "/tasks",
        params={"task": "Study DevOps"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task added",
        "tasks": ["Study DevOps"]
    }


def test_get_tasks():
    client.post(
        "/tasks",
        params={"task": "Learn FastAPI"}
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [
        "Learn FastAPI"
    ]


def test_get_task_by_index():
    client.post(
        "/tasks",
        params={"task": "Write tests"}
    )

    response = client.get("/tasks/0")

    assert response.status_code == 200
    assert response.json() == {
        "task": "Write tests"
    }


def test_delete_task():
    client.post(
        "/tasks",
        params={"task": "Delete this task"}
    )

    response = client.delete("/tasks/0")

    assert response.status_code == 200
    assert response.json() == {
        "removed": "Delete this task"
    }


def test_task_not_found():
    response = client.get("/tasks/99")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found"
    }