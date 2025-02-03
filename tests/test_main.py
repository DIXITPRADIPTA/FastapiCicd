from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "John Doe", "age": 20, "grade": "A"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_read_student():
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_student():
    response = client.put("/students/1", json={"name": "Jane Doe", "age": 21, "grade": "B"})
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_student():
    response = client.delete("/students/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"

def test_read_non_existent_student():
    response = client.get("/students/99")
    assert response.status_code == 404
