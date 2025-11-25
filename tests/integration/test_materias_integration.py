def test_create_materia_integration(client, materia_data):
    response = client.post("/materias/", json=materia_data)
    assert response.status_code == 200
    data = response.json()
    assert data["codigo"] == materia_data["codigo"]
    assert "id" in data

def test_get_materias_integration(client, materia_data):
    client.post("/materias/", json=materia_data)
    response = client.get("/materias/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["nombre"] == materia_data["nombre"]

def test_get_materia_by_id_integration(client, materia_data):
    create_response = client.post("/materias/", json=materia_data)
    materia_id = create_response.json()["id"]
    response = client.get(f"/materias/{materia_id}")
    assert response.status_code == 200
    assert response.json()["id"] == materia_id