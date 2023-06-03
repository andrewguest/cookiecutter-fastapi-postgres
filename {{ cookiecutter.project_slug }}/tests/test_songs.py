from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_index():
    response = client.get("/songs")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
