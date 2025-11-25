def test_create_tarea_integration(client, tarea_data):
    client.post("/alumnos/", json={"nombre": "Test", "email": "test@test.com"})
    client.post("/materias/", json={"nombre": "Test", "codigo": "TEST101"})
    response = client.post("/tareas/", json=tarea_data)
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == tarea_data["titulo"]

def test_calificar_tarea_integration(client, tarea_data):
    client.post("/alumnos/", json={"nombre": "Test", "email": "test@test.com"})
    client.post("/materias/", json={"nombre": "Test", "codigo": "TEST101"})
    create_response = client.post("/tareas/", json=tarea_data)
    tarea_id = create_response.json()["id"]
    response = client.put(f"/tareas/{tarea_id}/calificar?calificacion=8.5")
    assert response.status_code == 200
    assert response.json()["calificacion"] == 8.5
    
def test_update_tarea_integration(client, tarea_data):
    client.post("/alumnos/", json={"nombre": "Test", "email": "test@test.com"})
    client.post("/materias/", json={"nombre": "Test", "codigo": "TEST101"})
    
    create_response = client.post("/tareas/", json=tarea_data)
    tarea_id = create_response.json()["id"]
    
    update_data = {"titulo": "Tarea Modificada", "calificacion": 8.0}
    response = client.put(f"/tareas/{tarea_id}", json=update_data)
    
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarea Modificada"
    assert response.json()["calificacion"] == 8.0

def test_delete_tarea_integration(client, tarea_data):
    client.post("/alumnos/", json={"nombre": "Test", "email": "test@test.com"})
    client.post("/materias/", json={"nombre": "Test", "codigo": "TEST101"})
    
    create_response = client.post("/tareas/", json=tarea_data)
    tarea_id = create_response.json()["id"]
    
    response = client.delete(f"/tareas/{tarea_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Tarea eliminada correctamente"
    
    get_response = client.get(f"/tareas/{tarea_id}")
    assert get_response.status_code == 404