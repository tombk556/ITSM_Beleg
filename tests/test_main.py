from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """tests root URL: checks if the server is running or not
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Server is running"


def test_get_incident_by_number():
    response = client.get("/incident/get_incident_by_number/INC0010001")
    assert response.status_code == 200

def test_create_incident():
    """tests POST request for creating a new incident
    """
    test_data = {
        "short_description": "Test Incident Creation",
        "description": "Test Incident Creation"
    }

    response = client.post("/incident/create_incident", json=test_data)

    # Response Erfolgreich?
    assert response.status_code == 201, response.text

    # Daten korrekt?
    data = response.json()
    assert data["short_description"] == "Test Incident Creation"
    assert data["description"] == "Test Incident Creation"

