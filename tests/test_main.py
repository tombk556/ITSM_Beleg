from datetime import datetime
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#globale Variable für sys_id
test_sys_id = None

def test_read_root():
    """tests root URL: checks if the server is running or not
    """
    response = client.get("/")
    assert response.status_code == 200


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
    assert response.status_code == 201

    # Daten korrekt?
    data = response.json()
    
    assert data["short_description"] == "Test Incident Creation"
    assert data["description"] == "Test Incident Creation"
    
    # Test-Ausgabe
    print("\nIncident created: \n\t"+ "\n\t".join(f"{key}: {value}" for key, value in data.items()))

    #Anpassung der globale Variablen für sys_id
    global test_sys_id
    test_sys_id = data["sys_id"]


def test_update_incident():

    updated_data = {
        "short_description": f"Test Incident Update {datetime.now()}",
        "description": f"Test Incident Update {datetime.now()}"
    }
    
    response = client.patch(f"/incident/update_incident/{test_sys_id}", json=updated_data)

    # Überprüfe, ob der Update-Request erfolgreich war
    assert response.status_code == 200

    
    # neuen Datenn korrekt?
    data = response.json()

    assert data["short_description"] == updated_data["short_description"]
    assert data["description"] == updated_data["description"]

    #Test-Ausgabe
    print("\nIncident updated: \n\t"+ "\n\t".join(f"{key}: {value}" for key, value in data.items()))


def test_delete_incident():
    
    response = client.delete(f"/incident/delete_incident/{test_sys_id}")

    # Überprüfung, ob der Delete-Request erfolgreich war
    assert response.status_code == 204

    # Test-Ausgabe
    print(f"\nIncident deleted: {response.status_code}")