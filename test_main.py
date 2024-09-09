from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_all_blogs():
    response = client.get('/all')
    assert response.status_code ==200
